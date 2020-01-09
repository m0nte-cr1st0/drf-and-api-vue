<template>
    <div id="list-app" style="position:relative">
        <h1>Shipments list</h1>
        <router-link to="/shipments/create/"><button type="button" class="btn btn-info button_create">Create shipment</button></router-link>
        <table class="table table-hover">
        <thead>
          <tr>
            <th v-for="key in column_dict" class="blackborder" style='text-align:center'>
              {{ key }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(shipment, ind) in shipments_list">
            <td v-for="(title, key) in column_dict" class="blackborder">
              <span v-if="key=='number'"><b>{{ ind+1 }}</b></span>
              <span v-if="key=='title'"><router-link :to="{ name: 'shipment_detail', params: { id: shipment.id }}">{{shipment[key]}}</router-link></span>
              <span v-else>{{shipment[key]}}<span v-if="key=='weight'"> {{shipment.weight_lot_type}}</span></span>
            </td>
          </tr>
        </tbody>
      </table>

    </div>
</template>

<script>

    export default {
        name: "shipment_list",

        data() {
            return {
                  column_dict:{'number': '#', 'title':'Title', 'height_cm':'Height(cm)', 'weight':'Weight', 'color':'Color', 'author': 'Author'},
                shipments_list: [],
                hoverLocal: this.hover
            }
        },
        mounted() {
            axios.get('http://127.0.0.1:8001/shipments/').then(response => {
                this.shipments_list = response.data;
            }).catch(error => {
                if (!error.response) {
                    // network error
                    this.errorStatus = 'Error: Network Error';
                } else {
                    this.errorStatus = error.response.data.message;
                }
            })
            }


    };

</script>

<style scoped>

.blackborder{
    border: 1px solid black;
}

.button_create {
    position: absolute;
    min-width: 150px;
    width: 150px;
    right: 5%;
    margin-left: 90%;
    bottom: 100%;
}

</style>
