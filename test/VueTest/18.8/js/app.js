var app =new Vue({
    el: "#app",
    data: {
        math: 90,
        physics: 78,
        english: 56,
    },
    computed: {
        sum: function () {
            return parseFloat(this.math + this.physics + this.english)
        },
        average: function () {
          return Math.round(this.sum/3)
        }
    }
})