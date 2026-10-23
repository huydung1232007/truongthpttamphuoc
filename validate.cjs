const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync('test.html','utf8');
const scripts=[...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
for(const js of scripts)new vm.Script(js);
const elements=new Map();
function element(){return {getContext(){return {createLinearGradient(){return {addColorStop(){}}},fillRect(){},strokeRect(){},fillText(){},measureText(t){return {width:t.length*16}}}},toDataURL(){return 'data:image/png;base64,test'},click(){},innerHTML:'',value:'',dataset:{},classList:{add(){},remove(){},toggle(){},contains(){return false}},setAttribute(){},addEventListener(){},focus(){},contains(){return false}}}
const callbacks=[];
const ctx={setInterval(){return 1},clearInterval(){},console,structuredClone,URLSearchParams,Date,Set,JSON,String,Array,Math,Number,localStorage:{getItem(){return null},setItem(){}},sessionStorage:{getItem(){return null}},document:{createElement(){return element()},documentElement:element(),querySelector(s){if(!elements.has(s))elements.set(s,element());return elements.get(s)},querySelectorAll(){return []},addEventListener(){}},location:{hash:''},navigator:{},scrollTo(){},scrollY:0,addEventListener(){},setTimeout(fn){callbacks.push(fn)},IntersectionObserver:class{observe(){}},window:{}};
vm.createContext(ctx);
const main=scripts.find(s=>s.includes('const seed='));
vm.runInContext(main+`\n
$('#sb').onclick();$('#sq').value='ky niem';$('#sf').onsubmit({preventDefault(){}});if(!location.hash.includes('tim-kiem'))throw Error('search submit failed');
if(!P.home().includes('2012 – 2026'))throw Error('comparison missing');
if(!P.home().includes('facebook.com/plugins/video'))throw Error('video missing');
if(!P.newsd(2).includes('tp-anniv-gallery-track'))throw Error('photos missing');
if(!P.newsd(2).includes('Những bước chân đầu tiên'))throw Error('article missing');
if(!P.search('ky niem').includes('search-result-card'))throw Error('accentless search failed');
if(!P.search('zzzzzzzz').includes('Không tìm thấy kết quả'))throw Error('empty search failed');
if(DB.albums.find(a=>a.id===30).imgs.length!==16)throw Error('album missing');
P.gallery();P.ann();
openLb(30);lbGo(1);if(lbI!==1)throw Error('lightbox next failed');
if(!$('#lbi').innerHTML.includes('data:image/'))throw Error('lightbox image missing');
$('#slide-play').onclick();if(slideTimer===null)throw Error('slideshow failed');stopSlides();if(slideTimer!==null)throw Error('slideshow stop failed');if(!P.memories().includes('memory-canvas'))throw Error('memories missing');$('#memory-form').onsubmit({preventDefault(){}});
for(const page of ['ky-niem','gioi-thieu','tin-tuc','lien-he','quan-tri','thu-vien','thong-bao']){location.hash='#/'+page;route();if(!$('#main').innerHTML)throw Error('empty page '+page)}
console.log('PASS: script syntax, home, anniversary article, 6-photo album, lightbox navigation, accentless/empty search, preserved routes');
`,ctx);
// Drain list rendering callbacks to catch missing references.
while(callbacks.length)callbacks.shift()();
console.log('PASS: list rendering callbacks');
