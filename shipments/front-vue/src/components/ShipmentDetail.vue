{% load rest_framework %}
<template>
    <div class="ShipmentDetail">
    <div class="col-md-12" style="position: relative">
        <div>
            <router-link to="/shipments/"><button type="button" class="btn btn-secondary button_list">Shipments list</button></router-link>
            <router-link to="/shipments/create/"><button type="button" class="btn btn-info button_create">Create shipment</button></router-link>
        </div>
            <table class="table table-sm table-bordered col-md-6"">
              <tbody>
                <tr v-for="(ind, key) in column_dict">
                  <th scope="row">{{ ind }}</th>
                  <td v-if="key=='weight'">{{ shipment[key] }} {{shipment.weight_lot_type}}</td>
                  <td v-else>{{ shipment[key] }}</td>
                </tr>
              </tbody>
            </table>
            </div>
         <div class='edit_form col-md-12'>
            <div class="form-row" style="margin-bottom: 20px">
                <button type="button" class="btn btn-warning show" ref="button_edit" @click='show_form()'>{{ edit_text }}</button>
                <button type="button" class="btn btn-danger remove" @click='remove()'>Delete</button>
             </div>
            <form v-bind:style="{ display: show }">
                <div class="form-row">
                  <div class="form-group col-md-7">
                    <label for="FormControlInput1">Title</label>
                    <input type="text" class="form-control" id="FormControlInput1" placeholder="Enter title of shipments" v-model='shipment.title'>
                  </div>
                <div class="form-group col-md-5">
                    <label for="FormControlInput2">Author</label>
                  <input type="text" class="form-control" id="FormControlInput2" placeholder="Enter your name" v-model='shipment.author'></input>
                </div>
              </div>
                  <div class="form-row">
                      <div class="form-group col-md-9">
                        <label for="exampleFormControlInput1">Weight</label>
                        <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="Shipments weight"  v-model='shipment.weight'>
                      </div>
                      <div class="form-group col-md-3">
                        <label for="exampleFormControlSelect1">Lot select</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model='shipment.weight_lot_type'>
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
                        <input type="number" class="form-control" id="exampleFormControlInput1" placeholder="Shipments height (in cm)" v-model='shipment.height_cm'>
                      </div>

                      <div class="form-group col-md-3">
                        <label for="exampleFormControlSelect1">Color select</label>
                        <select class="form-control" id="exampleFormControlSelect1" v-model='shipment.color'>
                          <option>Black</option>
                          <option>Red</option>
                          <option>White</option>
                          <option>Other</option>
                        </select>
                      </div>
                  </div>
                              <div class="edit">
                <button type="button" class="btn btn-success save" @click='save_data()'>Save</button>
            </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Shipment',
    data() {
        return {
            column_dict:{'title':'Title', 'height_cm':'Height (cm)', 'weight':'Weight', 'color':'Color', 'author': 'Author'},
            shipment: {'title': 'asas', 'height_cm': 'fsdfsdf', 'weight': 'dasdasd', 'weight_lot_type': 'dasdasd', 'color': 'dasdasd', 'author': 'dasdasd'},
            show: 'none',
            edit_text: 'Edit'
        }
    },
    mounted() {
        let id = this.$route.params.id;
        axios.get('http://127.0.0.1:8001/shipments/'+id).then(response => {
            console.log(response)
            this.shipment = response.data;
        }).catch(error => {
            console.log(error)
            if (!error.response) {
                this.errorStatus = 'Error: Network Error';
            } else {
                this.errorStatus = error.response.data.message;
            }
        })
    },
    methods: {
        save_data() {
            axios.put('http://127.0.0.1:8001/shipments/', {
                title: this.shipment.title,
                height_cm: this.shipment.height_cm,
                weight:  this.shipment.weight,
                weight_lot_type: this.shipment.weight_lot_type,
                author: this.shipment.author,
                color: this.shipment.color,
                id: this.$route.params.id
                }).then(response => {
                    console.log(response)
                    location.reload()
                }).catch(error => {
                    console.log(error)
                    if (!error.response) {
                        this.errorStatus = 'Error: Network Error';
                    } else {
                        this.errorStatus = error.response.data.message;
                    }
            })
        },
        remove() {
            console.log(this.$route.params.id)
            axios.delete('http://127.0.0.1:8001/shipments/', {data: {id: this.$route.params.id}}
            ).then(response => {
                location.href = '/shipments/'
            })
        },
        show_form() {
            if (this.show=='block') {
                this.show='none';
                this.edit_text = 'Edit';
            } else {
                this.show='block';
                this.edit_text = 'Hide';
            }
        }
    }
};
</script>

<style scoped>
.table, .edit_form{
    width: 50%;
    left: 25%;
}

button {
    width: 25%;
    height: 40px;
    margin: 0 auto;
}

.button_top, .button_list, .button_create {
    position: absolute;
    bottom: 100%;
    min-width: 150px;
    width: 150px;
}
.button_list {
    left: 5%;
}

.button_create {
    right: 5%;
}
</style>
