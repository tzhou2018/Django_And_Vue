console.log('1:', 1);
var routes = [
    {
        path: '/',
        component: {
            template: '<h1>Home</h1>'
        }
    },
    {
        path: '/post',
        components: {
            sidebar: {
                template: '\
                <div>\
                <ul>\
                <li>帖子列表</li>\
                <li>标签管理</li>\
                 </ul>\
                 </div>   \
                 '
            },
            content: {
                template: '\
                <div>suisbhiai</div>'
            }
        }
    },
    {
        path: '/user',
        components: {
            sidebar: {
                template: '\
                <div>\
                <ul>\
                <li>用户列表</li>\
                <li>权限管理</li>\
                 </ul>\
                 </div>   \
                 '
            },
            content: {
                template: '\
                <div>suisbhiai</div>'
            }
        }
    },
    {
        path: '/about',
        component: {
            template: '' +
            '<div>\
                <h1>关于我们</h1>\
              </div>',
        },
    },
    {
        path: '/user/:name',
        name: 'user',
        component: {
            template: '' +
            '<div>' +
            '<div>我叫: {{ $route.params.name}}</div>' +
            // '<router-link :to="'/user/'+$router.params.name+ '/more'"> </router-link>' +
            '<router-link to="/more" append>更多信息</router-link>' +
            '<router-view></router-view>' +
            '</div>',
            // template: '\
            // <div>\
            //     <div>我叫: {{ $route.params.name}}</div>\
            //     <router-link :to="'/user/' + $route.params.name + '/more'"> </router-link>\
            //     <router-view></router-view>\
            //  </div>'


        },
        children: [
            {
                path: '/more',
                component: {
                    template: '\
                    <div>\
                    用户：{{$route.params.name}}的详细信息\
                    sjaofoahjfaljofuaojflahjfolajoljalfja\
                    </div>'
                }
            }
        ]
    },
    ];

    var router = new VueRouter({
        routes: routes,
    });

    new Vue({
        el: '#app',
        router: router,
        methods: {
            surf: function () {
                setTimeout(function () {
                    this.router.push('/about');
                    setTimeout(function () {
                        // this.router.push('/user/王花花');
                        this.router.push({name: 'user',params: {name: '王花花'}})
                    }, 2000)
                }, 2000)

            }
        }
    });
