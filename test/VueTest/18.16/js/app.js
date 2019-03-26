//自定义指令
//el 为整个属性 bindings为pin
Vue.directive('pin',function (el,binding) {
    var state=binding.value;
    var position = binding.modifiers;
    var warning = binding.arg;
    console.log('position:', position);


    if (state) {
        el.style.position='fixed';

        for (var key in position){
            if (position[key]) {
                el.style[key] = '10px';
            }
         }
         if (warning === 'true') {
            el.style.background = 'yellow';
         }
    }
    else
        el.style.position='static';


});
new Vue({
    el:'#app',
    data:{
        card1:false,
        card2:false,
    }
})