<template>
  <div class="home">
    <h1>Home Page</h1>
    <!-- This is where we would fetch data from Flask API -->
    <div v-if="loading">Loading...</div>
    <div v-else>
      <ul>
        <li v-for="item in items" :key="item.id">{{ item.name }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'HomeView',
  setup() {
    const items = ref([])
    const loading = ref(true)

    const fetchItems = async () => {
      try {
        const response = await axios.get('/api/items')
        items.value = response.data
      } catch (error) {
        console.error(error)
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      fetchItems()
    })

    return { items, loading }
  }
}
</script>

<style scoped>
/* Add some styling */
</style>
