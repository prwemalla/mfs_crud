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
    <b-row class="mt-2">
      <b-form-group id="status" label="Status" label-for="status">
        <b-form-select v-model="task.status" :options="options" class="mt-2" placeholder="Status"></b-form-select>
      </b-form-group>
    </b-row>
    <b-row class="mt-4">
      <b-col cols="3">
        <b-button variant="primary" class="px-5" @click="updateTask"
          >Edit Task</b-button
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
  props: {
    taskId: Number,
  },
  data() {
    return {
      task: {},
      options: [
        { value: 'PENDING', text: 'Pending' },
        { value: 'DONE', text: 'Done' }
      ]
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
          `http://127.0.0.1:8000/task_service/api/v1/task/${this.taskId}/`,
          { headers: { Authorization: 'Bearer ' + user.accessToken } }
        )
        .then((response) => {
          this.task = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateTask() {
      let user = JSON.parse(localStorage.getItem('user'));
      let task_data = this.task
      task_data.user = user.user_details.id
      axios
        .put(
          `http://127.0.0.1:8000/task_service/api/v1/task/${this.taskId}/`,
          task_data,
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