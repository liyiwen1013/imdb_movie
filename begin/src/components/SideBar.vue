<template>
<div>
    <el-container style="border: 1px solid #eee">
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
            <el-menu>
                <template index="1">
                    <router-link to="/home">
                        <el-menu-item index="1-1">
                            <i class="el-icon-message"></i>首页
                        </el-menu-item>
                    </router-link>
                </template>
                <el-submenu index="2">
                    <template slot="title"><i class="el-icon-menu"></i>数据展示</template>
                    <router-link to="/basicData">
                        <el-menu-item index="2-1">数据展示</el-menu-item>
                    </router-link>
                    <router-link to="/correlationAnalysis">
                        <el-menu-item index="2-2">相关性分析</el-menu-item>
                    </router-link>
                    <router-link to="/BoxOffice">
                        <el-menu-item index="2-3">影响票房因素</el-menu-item>
                    </router-link>
                    <router-link to="/PopularWel">
                        <el-menu-item index="2-4">影响受欢迎因素</el-menu-item>
                    </router-link>
                </el-submenu>
                <template index="3">
                    <router-link to="/SummaryAn">
                        <el-menu-item index="3-1">
                            <i class="el-icon-menu"></i>分析总结
                        </el-menu-item>
                    </router-link>
                </template>
            </el-menu>
        </el-aside>

        <el-container style="margin-top: 50px">
            <router-view></router-view>
        </el-container>
    </el-container>
</div>
</template>

<script>
export default {};
</script>

<style>
.el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
}

.el-aside {
    color: #333;
}

a {
    text-decoration: none
}
</style>

