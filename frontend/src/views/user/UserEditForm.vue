<template>
  <b-form class="mt-3">
    <b-row>
      <b-row>
        <h4 class="text-secondary">User Details</h4>
      </b-row>
      <b-col cols="6">
        <b-form-group id="first_name" label="First Name" label-for="first_name">
          <b-form-input
            id="first_name"
            type="text"
            placeholder="First Name"
            v-model="customer.first_name"
          ></b-form-input>
        </b-form-group>
      </b-col>
      <b-col cols="6">
        <b-form-group id="last_name" label="Last Name" label-for="last_name">
          <b-form-input
            id="last_name"
            type="text"
            placeholder="Last Name"
            v-model="customer.last_name"
          ></b-form-input>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row class="mt-3">
      <b-col cols="6">
        <b-form-group id="email" label="E-Mail" label-for="email">
          <b-form-input
            id="email"
            type="email"
            placeholder="example@crm.com"
            v-model="customer.email"
          ></b-form-input>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row class="mt-5">
      <h4 class="text-secondary">Access Details</h4>
    </b-row>
    <b-row class="mt-2">
      <b-form-checkbox
        id="customer_status"
        v-model="customer.is_active"
        name="customer-status"
        value=true
        unchecked-value=false
      >
        User is active
      </b-form-checkbox>
    </b-row>
    <b-row class="mt-2">
      <b-form-checkbox
        id="admin_status"
        v-model="customer.is_superuser"
        name="customer-status"
        value=true
        unchecked-value=false
      >
        User is Admin
      </b-form-checkbox>
    </b-row>
    <b-row class="mt-4">
      <b-col cols="3">
        <b-button variant="primary" class="px-5" @click="updateCustomer"
          >Update User</b-button
        >
      </b-col>
      <b-col>
        <b-button variant="warning" @click="triggerClose">Close</b-button>
      </b-col>
    </b-row>
  </b-form>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateCustomerModal",
  props: {
    customerId: Number,
  },
  data() {
    return {
      customer: {},
    };
  },
  mounted() {
    this.getCusomterByID();
  },
  methods: {
    triggerClose() {
      this.$emit("closeEditModal");
    },
    getCusomterByID() {
      let user = JSON.parse(localStorage.getItem('user'));
      axios
        .get(
          `http://localhost:8080/auth/api/v1/user/${this.customerId}/`,
          { headers: { Authorization: 'Bearer ' + user.accessToken } }
        )
        .then((response) => {
          this.customer = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateCustomer() {
      let user = JSON.parse(localStorage.getItem('user'));
      axios
        .put(
          `http://localhost:8080/auth/api/v1/user/${this.customerId}/`,
          this.customer,
          { headers: { Authorization: 'Bearer ' + user.accessToken } }
        )
        .then((response) => {
          console.log(response.data);
          this.$emit("closeEditModal");
          this.$emit("reloadDataTable");
          this.$emit("showSuccessAlert");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>