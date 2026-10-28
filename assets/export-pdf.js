/* Current-view export. All processing stays in the browser. */
(() => {
  const button = document.getElementById('print');
  const scriptCache = new Map();
  const assetBase = new URL('pdf/', document.currentScript.src);
  const status = document.createElement('p');
  status.id = 'pdf-status'; status.className = 'meta'; status.setAttribute('role','status');
  status.hidden = true;
  document.getElementById('study-tools').after(status);
  const notify = text => { status.textContent = text; status.hidden = false; };

  function dependency(file, globalName) {
    if (window[globalName]) return Promise.resolve(window[globalName]);
    if (!scriptCache.has(file)) scriptCache.set(file, new Promise((resolve,reject) => {
      const script = document.createElement('script');
      script.src = new URL(file,assetBase).href;
      script.onload = () => window[globalName] ? resolve(window[globalName]) : reject(new Error('PDF组件加载失败'));
      script.onerror = () => { script.remove(); scriptCache.delete(file); reject(new Error('PDF组件未加载成功，请检查网络后重试')); };
      document.head.append(script);
    }));
    return scriptCache.get(file);
  }
  function rows(table) {
    if (!table) return [];
    return Array.from(table.querySelectorAll('tbody tr'), row => ({
      word:row.querySelector('.word')?.textContent.trim().replace(/^★\s*/, '') || '',
      meaning:row.querySelector('.meaning')?.textContent.trim() || '',
      phonetic:row.querySelector('.phonetic')?.textContent.trim() || '',
      phrase:row.querySelector('.phrase')?.textContent.trim() || '',
      marked:row.classList.contains('marked'),
      priority:row.querySelector('.word')?.textContent.includes('★') || false,
    }));
  }
  function capture() {
    if (document.body.dataset.view === 'vocabulary') {
      const words=rows(document.querySelector('#vocab-table table'));
      return {title:'我的生词本',subtitle:`${words.length} 个生词 · 按英文字母顺序排列`,
        filename:'CET6_我的生词本.pdf',groups:[{title:'生词',rows:words}]};
    }
    const section=document.querySelector('.day:not([hidden])');
    if (!section || document.body.dataset.view !== 'day') throw new Error('请先选择一个学习日期，或打开我的生词再导出');
    const day=Number(section.id.slice(1));
    const date=new Date(Date.UTC(2026,9,26+day-1)).toISOString().slice(0,10);
    const groups=[];
    const newWords=rows(section.querySelector(':scope > .tablewrap table'));
    const oldWords=rows(section.querySelector('.daily-review table'));
    if(newWords.length)groups.push({title:`当天词汇 · ${newWords.length}词`,rows:newWords});
    if(oldWords.length)groups.push({title:`旧词复习 · ${oldWords.length}词`,rows:oldWords});
    if(!groups.length && day>=43 && day<=47) {
      for(const link of section.querySelectorAll(':scope > ul a[href^="#d"]')) {
        const target=document.getElementById(link.getAttribute('href').slice(1));
        const words=rows(target?.querySelector(':scope > .tablewrap table'));
        if(words.length)groups.push({title:target.querySelector('h3').textContent,rows:words});
      }
    }
    if(!groups.length && day===48)groups.push({title:'考前熟悉搭配',rows:Array.from(section.querySelectorAll(':scope > ul li'),li=>({word:li.textContent,meaning:'',phrase:'',marked:false,priority:false}))});
    const score=section.querySelector('.score');
    const subtitle=score && score.value!=='' && score.validity.valid ? `识义 ${score.value}/${score.max} · 日期 ${date}` : `日期 ${date}`;
    return {title:section.querySelector('h3').textContent,subtitle,filename:`CET6_${date}_学习词汇.pdf`,groups};
  }
  async function generate(snapshot) {
    const [lib,fontkit,fontBase64]=await Promise.all([
      dependency('pdf-lib.min.js','PDFLib'),dependency('fontkit.umd.min.js','fontkit'),
      dependency('font-data.js','CET6PdfFontBase64'),
    ]);
    const {PDFDocument,rgb}=lib;
    const pdf=await PDFDocument.create();
    pdf.registerFontkit(fontkit);
    const bytes=Uint8Array.from(atob(fontBase64),char=>char.charCodeAt(0));
    // Font assets are already subset at build time; embed complete TrueType files.
    const font=await pdf.embedFont(bytes,{subset:false});
    const ipaBytes=Uint8Array.from(atob(window.CET6IpaFontBase64),char=>char.charCodeAt(0));
    const ipaFont=await pdf.embedFont(ipaBytes,{subset:false});
    const primaryChars=new Set(font.getCharacterSet());
    const fallbackChars=new Set(ipaFont.getCharacterSet());
    function runs(value) {
      const result=[];
      for(const char of value) {
        const code=char.codePointAt(0);
        const selected=primaryChars.has(code)?font:(fallbackChars.has(code)?ipaFont:null);
        if(!selected)throw new Error('PDF 字体缺少字符：'+char);
        if(result.length && result[result.length-1].font===selected)result[result.length-1].value+=char;
        else result.push({font:selected,value:char});
      }
      return result;
    }
    const measure=(value,fontSize)=>runs(value).reduce((sum,run)=>sum+run.font.widthOfTextAtSize(run.value,fontSize),0);
    pdf.setTitle(snapshot.title); pdf.setAuthor('CET-6 词汇复习');
    const ink=rgb(.14,.21,.18),muted=rgb(.43,.49,.44),green=rgb(.20,.43,.33);
    const lineColor=rgb(.86,.89,.85),yellow=rgb(1,.95,.72);
    const W=841.89,H=595.28,left=36,right=W-36,bottom=42;
    const size=9.5,leading=14,padding=7;
    const widths=[32,155,175,185,right-left-32-155-175-185];
    let page,y;
    const clean=value=>String(value).replace(/[\u2010-\u2015]/g,'-').replace(/\u00a0/g,' ');
    const text=(value,x,baseline,fontSize=size,color=ink)=>{
      for(const run of runs(clean(value))){page.drawText(run.value,{x,y:baseline,size:fontSize,font:run.font,color});x+=run.font.widthOfTextAtSize(run.value,fontSize);}
    };
    function wrap(value,width,fontSize=size) {
      const result=[];
      for(const para of clean(value).split('\n')) {
        let line='';
        for(const ch of para) {
          if(line && measure(line+ch,fontSize)>width){result.push(line);line=ch;} else line+=ch;
        }
        result.push(line);
      }
      return result;
    }
    function newPage() {
      page=pdf.addPage([W,H]);y=H-42;
      text('CET-6 / VOCABULARY',left,y,9,green);y-=25;
    }
    function need(height){if(y-height<bottom)newPage();}
    function paragraph(value,fontSize=10,color=muted) {
      for(const line of wrap(value,right-left,fontSize)){need(fontSize+8);text(line,left,y,fontSize,color);y-=fontSize+7;}
    }
    function header(){
      need(30);page.drawRectangle({x:left,y:y-25,width:right-left,height:25,color:rgb(.94,.96,.93)});
      let x=left;['序号','英文 / ★优先运用','核心意思','音标（美式）','常用搭配'].forEach((value,index)=>{text(value,x+padding,y-16,9,green);x+=widths[index];});y-=25;
    }
    newPage();paragraph(snapshot.title,17,ink);y-=3;paragraph(snapshot.subtitle,10,muted);y-=8;
    for(const group of snapshot.groups) {
      need(75);paragraph(group.title,12,green);y-=4;
      if(!group.rows.length){paragraph('当前生词本暂无词汇。');continue;}
      header();
      group.rows.forEach((row,index)=>{
        const values=[String(index+1).padStart(2,'0'),(row.priority?'★ ':'')+row.word,row.meaning,row.phonetic || '',row.phrase];
        const lines=values.map((value,col)=>wrap(value,widths[col]-padding*2));
        const height=Math.max(1,...lines.map(list=>list.length))*leading+padding*2;
        if(y-height<bottom){newPage();paragraph(group.title+'（续）',11,green);header();}
        if(row.marked)page.drawRectangle({x:left,y:y-height,width:right-left,height,color:yellow});
        let x=left;
        lines.forEach((list,col)=>{list.forEach((line,n)=>text(line,x+padding,y-padding-size-n*leading));x+=widths[col];});
        page.drawLine({start:{x:left,y:y-height},end:{x:right,y:y-height},thickness:.5,color:lineColor});y-=height;
      });
      y-=20;
    }
    const pages=pdf.getPages();
    pages.forEach((sheet,index)=>{
      sheet.drawLine({start:{x:left,y:32},end:{x:right,y:32},thickness:.5,color:lineColor});
      sheet.drawText(`${index+1} / ${pages.length}`,{x:right-45,y:19,size:8,font,color:muted});
    });
    return pdf.save();
  }
  button.textContent='导出 PDF';button.title='将当前学习日或生词本保存为 PDF';
  button.addEventListener('click',async()=>{
    let handle=null;
    try {
      const snapshot=capture(); // Freeze the selected date/word list at click time.
      button.disabled=true;button.textContent='正在导出…';notify('正在准备当前页面的 PDF…');
      if(typeof window.showSaveFilePicker==='function') {
        try {handle=await window.showSaveFilePicker({suggestedName:snapshot.filename,types:[{description:'PDF 文档',accept:{'application/pdf':['.pdf']}}]});}
        catch(error){if(error.name==='AbortError')throw error;if(error.name!=='SecurityError')throw error;}
      }
      const bytes=await generate(snapshot);
      if(handle){const writable=await handle.createWritable();await writable.write(bytes);await writable.close();}
      else {
        const url=URL.createObjectURL(new Blob([bytes],{type:'application/pdf'}));
        const link=document.createElement('a');link.href=url;link.download=snapshot.filename;
        document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);
      }
      notify('PDF 已导出：'+snapshot.filename);
    } catch(error) {notify(error.name==='AbortError'?'已取消导出。':'导出失败：'+error.message);}
    finally {button.disabled=false;button.textContent='导出 PDF';}
  });
})();
