<template>
<div id="app">
    <v-sidebar></v-sidebar>
</div>
</template>

<script>
import SideBar from './components/SideBar.vue'
export default {
    components: {
        "v-sidebar": SideBar
    }
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
}
</style>
