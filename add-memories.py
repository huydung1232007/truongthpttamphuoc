from pathlib import Path
p=Path('test.html');s=p.read_text(encoding='utf-8')
css='''<style id="memories-style">
.memory-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin-top:26px}.memory-note{padding:26px;border:1px solid var(--b);border-radius:16px;background:var(--sf);box-shadow:var(--sh)}.memory-note .quote{font-size:2.4rem;color:var(--a);line-height:1}.memory-note p{margin:12px 0 18px}.memory-note small{color:var(--t2)}.memory-tools{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}.memory-maker{display:grid;grid-template-columns:minmax(240px,1fr) minmax(280px,1.4fr);gap:28px;align-items:start}.memory-maker canvas{width:100%;height:auto;border-radius:16px;box-shadow:var(--sh)}.lb .ct{flex-wrap:wrap;justify-content:center}.lb .im .th img{object-fit:contain!important;background:#101724}.memory-intro{color:var(--t2);max-width:65ch}@media(max-width:700px){.memory-maker{grid-template-columns:1fr}}
</style>
'''
s=s.replace('</head>',css+'</head>',1)
s=s.replace("['/thu-vien','Thư viện'],","['/thu-vien','Thư viện'],['/ky-niem','Kỷ niệm'],",1)
s=s.replace("'thu-vien':P.gallery,","'thu-vien':P.gallery,'ky-niem':P.memories,",1)
# Home entry before latest news.
anchor='<section class="sec"><div class="wrap"><div class="k">Tin tức</div>'
entry='''<section class="sec alt"><div class="wrap"><div class="k">Kết nối các thế hệ</div><h2 class="t">Gửi một lời thương về mái trường</h2><p class="memory-intro">Ba mươi năm, biết bao câu chuyện. Cùng đọc những lời gửi gắm và tạo tấm thiệp mang dấu ấn của riêng bạn.</p><div class="memory-tools"><a class="btn red" href="#/ky-niem">Sổ lưu bút & tạo thiệp</a><a class="btn out" href="#/thu-vien">Xem album kỷ niệm</a></div></div></section>'''
assert anchor in s;s=s.replace(anchor,entry+anchor,1)
code='''
      P.memories=()=>head('Kỷ niệm 30 năm','Kỷ niệm','Lưu giữ lời thương – Gửi trao ký ức')+`<section class="sec"><div class="wrap"><div class="k">Sổ lưu bút 30 năm</div><h2 class="t">Lời gửi gắm đến mái trường</h2><p class="memory-intro">Những lời chúc chung dành tặng thầy cô, bạn bè và các thế hệ học sinh Tam Phước.</p><div class="memory-grid">${[
['Tri ân thầy cô','Cảm ơn những người thầy, người cô đã kiên nhẫn dìu dắt, trao tri thức và thắp lên những ước mơ. Kính chúc thầy cô luôn mạnh khỏe, hạnh phúc và giữ mãi ngọn lửa yêu nghề.'],
['Thương nhớ tuổi học trò','Có những năm tháng đi qua nhưng tiếng trống trường, hàng ghế đá và nụ cười bạn bè vẫn còn ở lại. Mong mỗi lần trở về, chúng ta lại tìm thấy một phần thanh xuân nơi đây.'],
['Tiếp bước tương lai','Chúc mái trường Tam Phước tuổi 30 tiếp tục vững bước, nuôi dưỡng những tài năng và chắp cánh cho nhiều thế hệ học sinh tự tin viết nên câu chuyện của mình.']
].map(([title,body])=>`<article class="memory-note"><div class="quote" aria-hidden="true">“</div><h3>${title}</h3><p>${body}</p><small>Gửi thương về Tam Phước · 1996 – 2026</small></article>`).join('')}</div></div></section><section class="sec alt"><div class="wrap"><div class="k">Chia sẻ kỷ niệm</div><h2 class="t">Tấm thiệp của riêng bạn</h2><p class="memory-intro">Điền tên, niên khóa và lời chúc, rồi tải thiệp để gửi cho thầy cô, bạn bè.</p><div class="memory-maker"><form id="memory-form"><div class="fld"><label for="memory-name">Tên của bạn</label><input id="memory-name" maxlength="50" placeholder="Nhập tên của bạn"></div><div class="fld"><label for="memory-year">Niên khóa</label><input id="memory-year" maxlength="30" placeholder="Ví dụ: 2010 – 2013"></div><div class="fld"><label for="memory-message">Lời chúc</label><textarea id="memory-message" rows="4" maxlength="220">Tự hào mái trường Tam Phước. Chúc thầy cô và các thế hệ học sinh luôn vững bước, viết tiếp những ước mơ!</textarea></div><button class="btn red" type="submit">Tải thiệp PNG</button></form><canvas id="memory-canvas" width="1200" height="800" role="img" aria-label="Bản xem trước thiệp kỷ niệm 30 năm"></canvas></div></div></section>`;
      function bindMemoryCard(){
       const form=$('#memory-form');if(!form)return;
       const canvas=$('#memory-canvas'),ctx=canvas.getContext('2d');if(!ctx)return;
       function lines(text,x,y,max,lineHeight){let words=text.split(/\\s+/),line='';for(const word of words){let test=line?line+' '+word:word;if(ctx.measureText(test).width>max&&line){ctx.fillText(line,x,y);line=word;y+=lineHeight}else line=test}ctx.fillText(line,x,y);return y+lineHeight}
       function draw(){const g=ctx.createLinearGradient(0,0,1200,800);g.addColorStop(0,'#172f60');g.addColorStop(1,'#3158a3');ctx.fillStyle=g;ctx.fillRect(0,0,1200,800);ctx.strokeStyle='#dfbe79';ctx.lineWidth=2;ctx.strokeRect(30,30,1140,740);ctx.fillStyle='#dfbe79';ctx.font='bold 24px sans-serif';ctx.fillText('TRƯỜNG THPT TAM PHƯỚC',72,100);ctx.font='bold 100px sans-serif';ctx.fillText('30 NĂM',66,225);ctx.font='28px sans-serif';ctx.fillText('1996 – 2026  ·  TỰ HÀO & TIẾP BƯỚC',72,280);ctx.fillStyle='#ffffff';ctx.font='30px sans-serif';lines($('#memory-message').value.trim()||'Gửi thương về mái trường Tam Phước.',72,375,1030,46);ctx.fillStyle='#dfbe79';ctx.font='bold 28px sans-serif';ctx.fillText($('#memory-name').value.trim()||'Một người yêu mái trường',72,680);ctx.fillStyle='#dae4f5';ctx.font='24px sans-serif';ctx.fillText($('#memory-year').value.trim()?'Niên khóa: '+$('#memory-year').value.trim():'Mãi nhớ Tam Phước',72,724)}
       form.addEventListener('input',draw);form.onsubmit=e=>{e.preventDefault();draw();const link=document.createElement('a');link.download='ky-niem-30-nam-tam-phuoc.png';link.href=canvas.toDataURL('image/png');link.click();toast('Đã tạo thiệp để tải về')};draw();
      }
'''
s=s.replace('      P.nf=',code+'      P.nf=',1)
s=s.replace('      function bind(){','      function bind(){\n       bindMemoryCard();',1)
# Slideshow button and automatic advancement; stop on close, Escape, route change.
s=s.replace('<span id="lc"></span','<span id="lc"></span><button type="button" class="btn ol" id="slide-play" aria-pressed="false">▶ Trình chiếu</button>',1)
anchor='      let lbA,lbI;'
assert anchor in s
s=s.replace(anchor,"""      let slideTimer=null;
      function stopSlides(){if(slideTimer!==null)clearInterval(slideTimer);slideTimer=null;const button=$('#slide-play');button.textContent='▶ Trình chiếu';button.setAttribute('aria-pressed','false')}
      $('#slide-play').onclick=()=>{if(slideTimer!==null){stopSlides();return}$('#slide-play').textContent='Ⅱ Tạm dừng';$('#slide-play').setAttribute('aria-pressed','true');slideTimer=setInterval(()=>lbGo(1),3500)};
      document.addEventListener('keydown',e=>{if(e.key==='Escape')stopSlides()});
      addEventListener('hashchange',()=>{stopSlides();$('#lb').classList.remove('on')});
"""+anchor,1)
s=s.replace("$('#lx').onclick=()=>$('#lb').classList.remove('on');","$('#lx').onclick=()=>{stopSlides();$('#lb').classList.remove('on')};",1)
s=s.replace('function openLb(id){lbA=', 'function openLb(id){stopSlides();lbA=',1)
p.write_text(s,encoding='utf-8')
print('Implemented memories page, downloadable card and album slideshow.')
