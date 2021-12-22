<template>
  <div>
    <b-row>
      <b-alert v-model="showSuccessAlert" variant="success" dismissible>
        {{ alertMessage }}
      </b-alert>
    </b-row>
    <b-row>
      <task-overview
        :totalTasks="numberOfTasks"
        :activeTasks="activeTasks"
        @totalTasksIsActive="setFilterTotalIsActive"
        @activeTaskIsActive="setFilterActiveIsActive"
      ></task-overview>
    </b-row>
    <b-row class="mt-3">
      <b-card>
        <b-row align-h="between">
          <b-col cols="6">
            <h3>{{ tableHeader }}</h3>
          </b-col>
          <b-col cols="2">
            <b-row>
              <b-col>
                <b-button
                  variant="primary"
                  id="show-btn"
                  @click="showCreateModal"
                >
                  <b-icon-plus class="text-white"></b-icon-plus>
                  <span class="h6 text-white">New Task</span>
                </b-button>
              </b-col>
            </b-row>
          </b-col>
        </b-row>
        <b-row class="mt-3">
          <b-table
            striped
            hover
            :items="items"
            :fields="fields"
            class="text-center"
          >
            <template #cell(task_name)="data">
              {{
                `${data.item.name}`
              }}
            </template>
            <template #cell(status)="data">
              <b-icon-bookmark-check-fill
                variant="success"
                v-if="data.item.status === 'DONE'"
              ></b-icon-bookmark-check-fill>
              <b-icon-bookmark-x-fill
                variant="danger"
                v-else
              ></b-icon-bookmark-x-fill>
            </template>
            <template #cell(actions)="data">
              <b-row>
                <b-col cols="7">
                  <b-icon-pencil-square
                    class="action-item"
                    variant="primary"
                    @click="getRowData(data.item.id)"
                  ></b-icon-pencil-square>
                </b-col>
                <b-col cols="1">
                  <b-icon-trash-fill
                    class="action-item"
                    variant="danger"
                    @click="showDeleteModal(data.item.id)"
                  ></b-icon-trash-fill>
                </b-col>
              </b-row>
            </template>
          </b-table>
        </b-row>
      </b-card>
    </b-row>

    <!-- Modal for adding new Tasks -->
    <b-modal
      ref="create-task-modal"
      size="xl"
      hide-footer
      title="New Task"
    >
      <create-task-form
        @closeCreateModal="closeCreateModal"
        @reloadDataTable="getTaskData"
        @showSuccessAlert="showAlertCreate"
      ></create-task-form>
    </b-modal>

    <!-- Modal for updating Tasks -->
    <b-modal
      ref="edit-task-modal"
      size="xl"
      hide-footer
      title="Edit Task"
    >
      <edit-task-form
        @closeEditModal="closeEditModal"
        @reloadDataTable="getTaskData"
        @showSuccessAlert="showAlertUpdate"
        :taskId="taskId"
      ></edit-task-form>
    </b-modal>

    <!-- Delete Task Modal -->
    <b-modal
      ref="delete-task-modal"
      size="md"
      hide-footer
      title="Confirm Deletion"
    >
      <delete-task-modal
        @closeDeleteModal="closeDeleteModal"
        @reloadDataTable="getTaskData"
        @showDeleteAlert="showDeleteSuccessModal"
        :taskId="taskId"
      ></delete-task-modal>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import TaskOverview from "./TaskOverview.vue";
import CreateTaskForm from "./TaskCreateForm.vue";
import EditTaskForm from "./TaskEditForm.vue";
import DeleteTaskModal from "./TaskDeleteModal.vue";

export default {
  components: {
    TaskOverview,
    CreateTaskForm,
    EditTaskForm,
    DeleteTaskModal,
  },
  data() {
    return {
      // Note 'isActive' is left out and will not appear in the rendered table

      fields: [
        {
          key: "id",
          label: "ID",
          sortable: false,
        },
        {
          key: "name",
          label: "Task Name",
          sortable: false,
        },
        {
          key: "description",
          label: "Description",
          sortable: false,
        },
        {
          key: "status",
          label: "Task Status",
          sortable: false,
        },
        "actions",
      ],
      items: [],
      numberOfTasks: 0,
      activeTasks: 0,
      activeTasksData: [],
      taskId: 0,
      companySearchTerm: "",
      tableHeader: "",
      showSuccessAlert: false,
      alertMessage: "",
    };
  },
  mounted() {
    this.getTaskData();
  },
  methods: {
    showCreateModal() {
      this.$refs["create-task-modal"].show();
    },
    closeCreateModal() {
      this.$refs["create-task-modal"].hide();
    },
    getTaskData() {
      let user = JSON.parse(localStorage.getItem('user'));
      axios
        .get("http://127.0.0.1:8000/task_service/api/v1/task/", { headers: { Authorization: 'Bearer ' + user.accessToken } })
        .then((response) => {
          this.tableHeader = "Total Tasks";
          this.items = response.data;
          this.numberOfTasks = response.data.length;
          this.activeTasksData = response.data.filter(
            (item) => item.status === "PENDING"
          );
          this.activeTasks = this.activeTasksData.length;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getRowData(id) {
      this.$refs["edit-task-modal"].show();
      this.taskId = id;
    },
    closeEditModal() {
      this.$refs["edit-task-modal"].hide();
    },
    setFilterTotalIsActive() {
      this.tableHeader = "Total Tasks";
      this.getTaskData();
    },
    setFilterActiveIsActive() {
      this.tableHeader = "Active Tasks";
      this.items = this.activeTasksData;
    },
    showAlertCreate() {
      this.showSuccessAlert = true;
      this.alertMessage = "Task was created successfully!";
    },
    showAlertUpdate() {
      this.showSuccessAlert = true;
      this.alertMessage = "Task was updated successfully";
    },
    showDeleteModal(id) {
      this.$refs["delete-task-modal"].show();
      this.taskId = id;
    },
    closeDeleteModal() {
      this.$refs["delete-task-modal"].hide();
    },
    showDeleteSuccessModal() {
      this.showSuccessAlert = true;
      this.alertMessage = "Task was deleted successfully!";
    },
  },
};
</script>

<style>
.action-item:hover {
  cursor: pointer;
}
</style>