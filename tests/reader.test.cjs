const {test} = require('node:test');
const assert = require('node:assert/strict');
const reader = require('../web/reader.js');
function event(key, extras={}) {return {key,target:{closest:()=>null},...extras};}
test('E expands and C collapses; unrelated keys pass through',()=>{
  assert.equal(reader.shortcutAction(event('e'),true),'expand');
  assert.equal(reader.shortcutAction(event('c'),true),'collapse');
  assert.equal(reader.shortcutAction(event('x'),true),null);
});
test('modifier combinations, repeat, composition, disabled shortcuts never trigger',()=>{
  for(const key of ['ctrlKey','metaKey','altKey','shiftKey','repeat','isComposing','defaultPrevented'])
    assert.equal(reader.shortcutAction(event('e',{[key]:true}),true),null,key);
  assert.equal(reader.shortcutAction(event('c'),false),null);
});
test('input, select, textarea and contenteditable targets are excluded',()=>{
  for(const target of [{closest:()=>({})},{isContentEditable:true,closest:()=>null}])
    assert.equal(reader.shortcutAction(event('e',{target}),true),null);
  assert.equal(reader.isEditable(null),false);
});
test('search is case-insensitive, multi-term, and combines with category',()=>{
  assert.equal(reader.matches('Self Forcing 自生成历史','少步蒸馏','SELF 历史','少步蒸馏'),true);
  assert.equal(reader.matches('Self Forcing','少步蒸馏','missing',''),false);
  assert.equal(reader.matches('Self Forcing','少步蒸馏','self','流式系统'),false);
});
function fakeDocument(){
  function control(value=''){return {value,hidden:false,checked:true,events:{},addEventListener(k,f){this.events[k]=f;}};}
  const controls=Object.fromEntries(['search','category','priority','result-count','empty','expand','collapse','shortcuts'].map(k=>[k,control()]));
  const cards=['Alpha 视频','Beta 系统'].map((s,i)=>({dataset:{search:s.toLowerCase(),category:i?'流式系统':'少步蒸馏',priority:i?'P2':'P0'},hidden:false,detail:{open:false},querySelector(){return this.detail;}}));
  return {cards,controls,events:{},querySelectorAll(){return cards;},getElementById(k){return controls[k];},addEventListener(k,f){this.events[k]=f;}};
}
test('real controller wires filters, empty state, buttons, and keyboard',()=>{
  const doc=fakeDocument();reader.init(doc);
  assert.equal(doc.controls['result-count'].textContent,'2 / 2 篇论文');
  doc.controls.search.value='alpha';doc.controls.search.events.input();
  assert.equal(doc.cards[0].hidden,false);assert.equal(doc.cards[1].hidden,true);
  doc.controls.expand.events.click();assert.ok(doc.cards.every(c=>c.detail.open));
  let prevented=false;doc.events.keydown(event('c',{preventDefault(){prevented=true;}}));
  assert.ok(prevented);assert.ok(doc.cards.every(c=>!c.detail.open));
  doc.controls.category.value='流式系统';doc.controls.category.events.change();
  assert.equal(doc.controls.empty.hidden,false);
  doc.controls.shortcuts.checked=false;doc.events.keydown(event('e',{preventDefault(){throw Error('disabled');}}));
  assert.ok(doc.cards.every(c=>!c.detail.open));
  doc.controls.collapse.events.click();assert.ok(doc.cards.every(c=>!c.detail.open));
});

test('priority combines with search and category without resetting expanded state',()=>{
  const doc=fakeDocument();reader.init(doc);
  doc.controls.expand.events.click();
  doc.controls.priority.value='P0';doc.controls.priority.events.change();
  assert.equal(doc.controls['result-count'].textContent,'1 / 2 篇论文');
  assert.equal(doc.cards[0].hidden,false);assert.equal(doc.cards[1].hidden,true);
  doc.controls.category.value='流式系统';doc.controls.category.events.change();
  assert.equal(doc.controls.empty.hidden,false);
  doc.controls.priority.value='';doc.controls.priority.events.change();
  assert.equal(doc.cards[1].hidden,false);
  assert.ok(doc.cards.every(c=>c.detail.open));
});
