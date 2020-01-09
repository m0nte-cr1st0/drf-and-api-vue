<template>
    <div class="ShipmentCreate" style="position:relative">
    <router-link to="/shipments/"><button type="button" class="btn btn-secondary button_list">Shipments list</button></router-link>
    <div class='edit_form col-md-12'>
        <p v-if="errors">
        <ul>
          <li v-for="(error, title) in errors" v-if="title!='height_cm'"><b>{{ title | capitalize }}</b> - <span style="color:red">{{ error }}</span></li>
          <li v-else><b>Height</b> - <span style="color:red">{{ error }}</span></li>
        </ul>
      </p>
        <form>
                <div class="form-row">
                  <div class="form-group col-md-7">
                    <label for="FormControlInput1">Title</label>
                    <input type="text" class="form-control" id="FormControlInput1" placeholder="Enter title of shipments" v-model='title'>
                  </div>
                <div class="form-group col-md-5">
                    <label for="FormControlInput2">Author</label>
                  <input type="text" class="form-control" id="FormControlInput2" placeholder="Enter your name" v-model='author'></input>
                </div>
              </div>
                  <div class="form-row">
                      <div class="form-group col-md-9">
                        <label for="exampleFormControlInput1">Weight</label>
                        <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="Shipments weight"  v-model='weight'>
                      </div>
                      <div class="form-group col-md-3">
                        <label for="exampleFormControlSelect1">Lot select</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model='weight_lot_type'>
                          <option>lb.</option>
                          <option>ton</option>
                          <option>kg.</option>
                          <option>g</option>
                        </select>
                      </div>
                  </div>
                  <div class="form-row">
                      <div class="form-group col-md-9">
                        <label for="exampleFormControlInput1">Height</label>
                        <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="Shipments height (in cm)" v-model='height_cm'>
                      </div>

                      <div class="form-group col-md-3">
                        <label for="exampleFormControlSelect1">Color select</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model='color'>
                          <option>Black</option>
                          <option>Red</option>
                          <option>White</option>
                          <option>Other</option>
                        </select>
                      </div>
                  </div>
            </form>
            <div class="edit">
                <button type="button" class="btn btn-success save" @click='save_data()'>Save</button>
            </div>
            </div>
    </div>
</template>

<script>
    export default {
        name: 'Shipment_create',
        data() {
            return {
                shipment: [],
                errors: [],
                title: this.title,
                height_cm: this.height_cm,
                weight: this.weight,
                weight_lot_type: "kg.",
                color: "Black",
                author: this.author
            }
        },
        methods: {
            save_data() {
                axios.post('http://127.0.0.1:8001/shipments/', {
                    title: this.title,
                    height_cm: this.height_cm,
                    weight:  this.weight,
                    weight_lot_type: this.weight_lot_type,
                    color: this.color,
                    author: this.author
                }).then(response => {
                    console.log(response)
                    location.href = 'http://127.0.0.1:8081/shipments/'
                }).catch(error => {
                   console.log(error.response.data)
                    this.errors = error.response.data;
                    console.log(this.errors)
                    if (!error.response) {
                        this.errorStatus = 'Error: Network Error';
                    } else {
                        this.errorStatus = error.response.data.message;
                    }
                })
            }
        },
        filters: {
          capitalize: function (value) {
            if (!value) return ''
            value = value.toString()
            return value.charAt(0).toUpperCase() + value.slice(1)
          }
      }
    };
</script>

<style scoped>
form{
    width: 50%;
    margin-left: 25%;
}

li {
    list-style-type: none;
}

.button_list {
    position: absolute;
    min-width: 150px;
    width: 150px;
    right: 5%;
    margin-left: 90%;
    bottom: 100%;
}

</style>
