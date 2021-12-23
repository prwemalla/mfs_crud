<template>
  <div>
    <b-row class="mt-2 mb-3">
      <h6 class="text-secondary">
        Are you sure you want to delete this User?
      </h6>
    </b-row>
    <b-row class="mt-2 mb-3">
      <p class="text-danger">
        This action is not reversible and may result in the loss if important
        data.
      </p>
    </b-row>
    <b-row class="mt-4">
      <b-col>
        <b-button variant="danger" @click="removeCustomerFromData"
          >Delete User</b-button
        >
      </b-col>
      <b-col>
        <b-button variant="warning" @click="triggerClose">Close</b-button>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DeleteCustomerModal",
  props: {
    customerId: Number,
  },
  methods: {
    triggerClose() {
      this.$emit("closeDeleteModal");
    },
    removeCustomerFromData() {
      let user = JSON.parse(localStorage.getItem('user'));
      axios
      .delete(
        `http://localhost:8080/auth/api/v1/user/${this.customerId}/`,
        { headers: { Authorization: 'Bearer ' + user.accessToken } }
        )
        .then(() => {
          this.$emit("reloadDataTable");
          this.$emit("showDeleteAlert");
          this.$emit("closeDeleteModal");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>