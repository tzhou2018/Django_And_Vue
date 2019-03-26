Vue.component('balance',{
    template:'\
    <div>\
        <show @show-balance="show_balance"></show>\
        <div v-if="show">\
        您的余额为：￥89\
        </div> \
    </div>',
    methods: {
        show_balance: function (data1) {
            this.show = true
            console.log('log:', data1);
        }
    },
    data: function () {
        return {
            show: false
        }
    }

});
Vue.component('show',{
    template: '<button @click="on_click">显示余额</button>',
    methods: {
        on_click:function () {


            // $emit相当于快捷方式，快速触发
            this.$emit('show-balance', {a:1, b:2})
        }
    }
})
new Vue({
    el: '#app'
})
//界面显示子组件，通过点击事件传递给父组件，父组件显示余额