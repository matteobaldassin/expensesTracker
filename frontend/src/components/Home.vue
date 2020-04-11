// Home.vue
<template>
  <div class="container">
    <h1>Expenses Tracker</h1>
    <hr />
    <b-button
      v-b-modal.add-category-modal
      type="button"
      class="btn btn-success btn-sm"
      >Aggiungi categoria</b-button
    >
    <hr />
    <b-form-select v-model="selected">
      <option
        v-for="category in categories"
        v-bind:key="category.category_id"
        v-bind:value="category.name"
      >
        {{ category.name }}
      </option>
    </b-form-select>
    <table class="table table-hover">
      <tr>
        <th scope="col">Nome</th>
        <th scope="col">Descrizione</th>
        <th scope="col">Paperback</th>
      </tr>
      <tbody>
        <tr v-for="(category, index) in categories" :key="index">
          <td>{{ category.name }}</td>
          <td>{{ category.description }}</td>
          <td>
            <button type="button" class="btn btn-info btn-sm">Update</button>
            <button type="button" class="btn btn-danger btn-sm">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <b-modal
      id="add-category-modal"
      title="Aggiungi nuova categoria"
      hide-footer
    >
      <form v-on:submit.prevent="add_category">
        <label for="category-name-input">Nome:</label>
        <input
          v-model="category_name"
          type="text"
          class="form-control"
          id="category-name-input"
          placeholder="Nome della categoria"
          required
        />
        <label for="category-description-input">Descrizione:</label>
        <input
          v-model="category_description"
          type="text"
          class="form-control"
          id="category-description-input"
        />
        <label for="category-color-input">Colore:</label>
        <input
          v-model="category_color"
          type="text"
          class="form-control"
          id="category-color-input"
        />
        <button type="submit" class="btn btn-success btn-block mt-3">
          Submit
        </button>
      </form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      categories: [],
      category_name: '',
      category_description: '',
      category_color: ''
    }
  },
  methods: {
    get_categories() {
      const path = `http://localhost:5000/API/categories`
      axios
        .get(path)
        .then(response => {
          this.categories = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    add_category() {
      const path = 'http://localhost:5000/API/categories'
      axios
        .post(path, {
          name: this.category_name,
          description: this.category_description,
          color: this.category_color
        })
        .then(() => {
          console.log('post success')
          this.get_categories()
          this.$bvModal.hide('add-category-modal')
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error)
          this.get_categories()
        })
    }
  },
  created() {
    this.get_categories()
  }
}
</script>
