//mixins 混合
// 重复功能的存储器
var base = {
    methods: {
        show: function () {
            this.visible = true;
        },
        hide: function () {
            this.visible = false;
        },
        toggle: function () {
            this.visible = !this.visible;
        },
    },
    data: function () {
        return {
            visible: false,
        }
    }
};
Vue.component('tooltip',{
    template: '\
    <div>\
        <span @mouseenter="show" @mouseleave = "hide">Solarzhou</span>\
        <div v-if="visible">周童</div>\
    </div>\
    ',
    mixins: [base],
    //明确定义将会覆盖base中定义的
    data: function () {
        return {
            visible: true,
        }
    }
});
Vue.component('popup', {
    template:'\
    <div>\
        <button @click="toggle">Popup</button>\
            <div v-if="visible">\
            <span @click="hide">X</span>\
                <h4>title</h4>\
             abcdefghigklmnopqrstuvwxyz\
             </div>\
    </div>\
    ',
    mixins: [base]

});
new Vue({
    el:'#app',
    data:{

    }
});