<template>
  <b-form class="mt-3">
    <b-row>
      <b-row>
        <h4 class="text-secondary">Task Details</h4>
      </b-row>
      <b-col cols="6">
        <b-form-group id="name" label="Task Name" label-for="name">
          <b-form-input
            id="name"
            type="text"
            placeholder="Task Name"
            v-model="task.name"
          ></b-form-input>
        </b-form-group>
      </b-col>
      <b-col cols="6">
        <b-form-group id="description" label="Description" label-for="description">
          <b-form-input
            id="description"
            type="text"
            placeholder="Description"
            v-model="task.description"
          ></b-form-input>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row class="mt-4">
      <b-col cols="3">
        <b-button variant="primary" class="px-5" @click="addNewTask"
          >Add Task</b-button
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
  name: "CreateTaskModal",
  data() {
    return {
      task: {},
    };
  },
  methods: {
    triggerClose() {
      this.$emit("closeCreateModal");
    },
    addNewTask() {
      let user = JSON.parse(localStorage.getItem('user'));
      let task_data = this.task
      task_data.user = user.user_details.id
      task_data.status = 'PENDING'
      axios
        .post("http://127.0.0.1:8000/task_service/api/v1/task/", task_data, { headers: { Authorization: 'Bearer ' + user.accessToken } })
        .then((response) => {
          this.$emit("closeCreateModal");
          this.$emit("reloadDataTable");
          this.$emit("showSuccessAlert");
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
  },
};
</script>