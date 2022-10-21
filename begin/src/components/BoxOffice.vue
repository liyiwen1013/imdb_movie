<template>
<div style="text-align: center">
    <div class="name">票房前十的电影</div>
    <v-chart :options="options5" style="display: inline-block; margin: 10px auto; width: 900px; height: 500px;" />
    <div class="name">票房前十的电影喜欢的人数</div>
    <v-chart :options="options6" style="display: inline-block; margin: 60px auto; width: 900px; height: 500px;" />
    <!-- <div class="summary">由此可见，美国出品电影数量占比最多，几乎占领了国际上电影的一大部分</div> -->
    <div class="name">票房与各数据的相关性分析</div>
    <v-chart :options="options2" style="display: inline-block; margin: 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options3" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options4" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options7" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options8" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
    <v-chart :options="options9" style="display: inline-block; margin: 0 120px 100px 120px; width: 900px; height: 500px;" />
</div>
</template>

<script>
import Axios from 'axios';
export default {
    data() {
        return {
            options5: {
                title: {
                },
                tooltip: {
                    show: true, // 是否显示
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    formatter: function (arg) {
                        return arg.name + ' 票房：' + arg.data
                    },
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'shadow', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    },
                    renderMode: 'html', // 浮层的渲染模式，默认以 'html 即额外的 DOM 节点展示 tooltip；
                    backgroundColor: 'rgba(50,50,50,0.7)', // 提示框浮层的背景颜色。
                    borderColor: '#333', // 提示框浮层的边框颜色。
                    borderWidth: 0, // 提示框浮层的边框宽。
                    padding: 5, // 提示框浮层内边距，
                    textStyle: { // 提示框浮层的文本样式。
                        color: '#fff',
                        fontStyle: 'normal',
                        fontWeight: 'normal',
                        fontFamily: 'sans-serif',
                        fontSize: 14,
                    }
                }, //可选，取决于有无提示框
                legend: {
                    type: 'plain', //----图例类型，默认为'plain'，当图例很多时可使用'scroll'
                    top: '1%', //----图例相对容器位置,top\bottom\left\right
                    textStyle: { //----图例内容样式
                        color: '#000', //---所有图例的字体颜色
                    }
                }, //可选，取决于有无图例
                xAxis: {
                    type: "category",
                    show: true, //---是否显示
                    name: '电影名', //---轴名称
                    position: 'bottom', //---x轴位置'top','bottom'
                    offset: 15, //---x轴相对于默认位置的偏移
                    nameLocation: 'end', //---轴名称相对位置'start','center','end'
                    nameTextStyle: { //---坐标轴名称样式
                        color: "#000",
                        padding: [5, 0, 0, -5], //---坐标轴名称相对位置
                    },
                    nameGap: 15, //---坐标轴名称与轴线之间的距离
                    nameRotate: 0, //---坐标轴名字旋转
                    axisLabel: {
                        interval: 0, //如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推。
                        rotate: '15', // 刻度标签旋转的角度,在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠。
                    },
                    data: []
                },
                yAxis: {
                    name: "票房（美元）"
                },
                grid: {
                    show: false, //---是否显示直角坐标系网格
                    top: 110, //---相对位置，top\bottom\left\right  
                    bottom: '30%',
                    height: 200,
                    tooltip: { //---鼠标焦点放在图形上，产生的提示框
                        show: true,
                        trigger: 'item', //---触发类型
                        textStyle: { //---提示框样式
                            color: '#fff',
                        },
                    }
                }, //位置设置
                series: {
                    type: 'bar',
                    //折线拐点标志的样式 
                    itemStyle: {
                        normal: {
                            color: function (params) {
                                var colorList = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622'];
                                // var colorList = ['#c23531','#2f4554', '#61a0a8'];
                                // 自动循环已经有的颜色
                                return colorList[params.dataIndex % colorList.length];
                            }
                        }
                    },
                    label: {
                        show: true,
                        position: 'top'
                    },
                    data: []
                }
            },
            options6: {
                title: {
                    text: '喜欢人数'
                },
                legend: {},
                tooltip: {},
                dataset: {
                    dimensions: [],
                    source: []
                },
                xAxis: {
                    type: 'category',
                    name: "电影名",
                    position: 'bottom', //---x轴位置'top','bottom'
                    offset: 15, //---x轴相对于默认位置的偏移
                    nameLocation: 'end', //---轴名称相对位置'start','center','end'
                    nameTextStyle: { //---坐标轴名称样式
                        color: "#000",
                        padding: [5, 0, 0, -5], //---坐标轴名称相对位置
                    },
                    nameGap: 15, //---坐标轴名称与轴线之间的距离
                    nameRotate: 0, //---坐标轴名字旋转
                    axisLabel: {
                        interval: 0, //如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推。
                        rotate: '15', // 刻度标签旋转的角度,在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠。
                    },
                },
                yAxis: {
                    name: "人"
                },
                grid: {
                    show: false, //---是否显示直角坐标系网格
                    top: 80, //---相对位置，top\bottom\left\right  
                    bottom: '30%',
                    tooltip: { //---鼠标焦点放在图形上，产生的提示框
                        show: true,
                        trigger: 'item', //---触发类型
                        textStyle: { //---提示框样式
                            color: '#fff',
                        },
                    }
                },
                series: [{
                    type: 'bar'
                }, {
                    type: 'bar'
                }, {
                    type: 'bar'
                }, {
                    type: 'bar'
                }, {
                    type: 'bar'
                }, {
                    type: 'bar'
                }]
            },
            options2: {
                title: {
                    text: '与电影时长'
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    }
                },
                xAxis: {
                    name: '电影时长'
                },
                yAxis: {
                    name: '票房'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options3: {
                title: {
                    text: '与电影imdb评分'
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    }
                },
                xAxis: {
                    name: 'imdb评分'
                },
                yAxis: {
                    name: '票房'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options4: {
                title: {
                    text: '与投票用户数'
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    }
                },
                xAxis: {
                    name: '投票数'
                },
                yAxis: {
                    name: '票房'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options7: {
                title: {
                    text: '与评论的用户数'
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    }
                },
                xAxis: {
                    name: '评论用户数'
                },
                yAxis: {
                    name: '票房'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options8: {
                title: {
                    text: '与评论的评分数量'
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    }
                },
                xAxis: {
                    name: '评分数量'
                },
                yAxis: {
                    name: '票房'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
            options9: {
                title: {
                    text: '与脸书喜欢人数'
                },
                tooltip: {
                    extraCssText: 'box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);', // 额外附加到浮层的 css 样式
                    confine: false, // 是否将 tooltip 框限制在图表的区域内。
                    trigger: 'axis', // 触发类型  'item'图形触发：散点图，饼图等无类目轴的图表中使用； 'axis'坐标轴触发；'none'：什么都不触发。
                    axisPointer: { // 坐标轴指示器配置项。
                        type: 'cross', // 'line' 直线指示器  'shadow' 阴影指示器  'none' 无指示器  'cross' 十字准星指示器。
                        axis: 'auto', // 指示器的坐标轴。 
                        snap: true, // 坐标轴指示器是否自动吸附到点上
                    }
                },
                xAxis: {
                    name: '脸书喜欢人数'
                },
                yAxis: {
                    name: '票房'
                },
                series: {
                    symbolSize: 10,
                    data: [],
                    type: 'scatter'
                }
            },
        }
    },
    mounted: function () {
        var api3 = "http://127.0.0.1:8000/api/test3";
        Axios.get(api3).then((response) => {
            console.log(response.data)
            const self = this;
            self.options5.xAxis.data = response.data.list1
            self.options5.series.data = response.data.list2
        })
        var api4 = "http://127.0.0.1:8000/api/test7";
        Axios.get(api4).then((response) => {
            this.options6.dataset.dimensions = response.data.list
            this.options6.dataset.source = response.data.set
        })
        var api2 = "http://127.0.0.1:8000/api/test10";
        Axios.get(api2).then((response) => {
            console.log(response.data)
            this.options2.series.data = response.data.list1
            this.options3.series.data = response.data.list2
            this.options4.series.data = response.data.list3
            this.options7.series.data = response.data.list4
            this.options8.series.data = response.data.list5
            this.options9.series.data = response.data.list6
        })

    }
}
</script>

<style>

</style>
