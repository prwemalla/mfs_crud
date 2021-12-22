<template>
  <div>
    <b-row>
      <b-alert v-model="showSuccessAlert" variant="success" dismissible>
        {{ alertMessage }}
      </b-alert>
    </b-row>
    <b-row>
      <customer-overview
        :totalCustomers="numberOfCustomers"
        :activeCustomers="activeCustomers"
        @totalCustomersIsActive="setFilterTotalIsActive"
        @activeCustomerIsActive="setFilterActiveIsActive"
      ></customer-overview>
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
                  <span class="h6 text-white">New User</span>
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
            <template #cell(contact_name)="data">
              {{
                `${data.item.contact_firstname} ${data.item.contact_lastname}`
              }}
            </template>
            <template #cell(customer_status)="data">
              <b-icon-bookmark-check-fill
                variant="success"
                v-if="data.item.customer_status === 'active'"
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

    <!-- Modal for adding new Users -->
    <b-modal
      ref="create-customer-modal"
      size="xl"
      hide-footer
      title="New User"
    >
      <create-customer-form
        @closeCreateModal="closeCreateModal"
        @reloadDataTable="getCustomerData"
        @showSuccessAlert="showAlertCreate"
      ></create-customer-form>
    </b-modal>

    <!-- Modal for updating Users -->
    <b-modal
      ref="edit-customer-modal"
      size="xl"
      hide-footer
      title="Edit Customer"
    >
      <edit-customer-form
        @closeEditModal="closeEditModal"
        @reloadDataTable="getCustomerData"
        @showSuccessAlert="showAlertUpdate"
        :customerId="customerId"
      ></edit-customer-form>
    </b-modal>

    <!-- Delete Customer Modal -->
    <b-modal
      ref="delete-customer-modal"
      size="md"
      hide-footer
      title="Confirm Deletion"
    >
      <delete-customer-modal
        @closeDeleteModal="closeDeleteModal"
        @reloadDataTable="getCustomerData"
        @showDeleteAlert="showDeleteSuccessModal"
        :customerId="customerId"
      ></delete-customer-modal>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import CustomerOverview from "./UserOverview.vue";
import CreateCustomerForm from "./UserCreateForm.vue";
import EditCustomerForm from "./UserEditForm.vue";
import DeleteCustomerModal from "./UserDeleteModal.vue";

export default {
  components: {
    CustomerOverview,
    CreateCustomerForm,
    EditCustomerForm,
    DeleteCustomerModal,
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
          key: "first_name",
          label: "First Name",
          sortable: false,
        },
        {
          key: "last_name",
          label: "Last Name",
          sortable: false,
        },
        {
          key: "email",
          label: "Email",
          sortable: false,
        },
        {
          key: "is_active",
          label: "Active",
          sortable: false,
        },
        {
          key: "is_superuser",
          label: "Admin",
          sortable: false,
        },
        "actions",
      ],
      items: [],
      numberOfCustomers: 0,
      activeCustomers: 0,
      activeCustomersData: [],
      customerId: 0,
      companySearchTerm: "",
      tableHeader: "",
      showSuccessAlert: false,
      alertMessage: "",
    };
  },
  mounted() {
    this.getCustomerData();
  },
  methods: {
    showCreateModal() {
      this.$refs["create-customer-modal"].show();
    },
    closeCreateModal() {
      this.$refs["create-customer-modal"].hide();
    },
    getCustomerData() {
      let user = JSON.parse(localStorage.getItem('user'));
      axios
        .get("http://localhost:8080/auth/api/v1/user/", { headers: { Authorization: 'Bearer ' + user.accessToken } })
        .then((response) => {
          this.tableHeader = "Total Users";
          this.items = response.data;
          this.numberOfCustomers = response.data.length;
          this.activeCustomersData = response.data.filter(
            (item) => item.is_active === true
          );
          this.activeCustomers = this.activeCustomersData.length;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getRowData(id) {
      this.$refs["edit-customer-modal"].show();
      this.customerId = id;
    },
    closeEditModal() {
      this.$refs["edit-customer-modal"].hide();
    },
    setFilterTotalIsActive() {
      this.tableHeader = "Total Users";
      this.getCustomerData();
    },
    setFilterActiveIsActive() {
      this.tableHeader = "Active Users";
      this.items = this.activeCustomersData;
    },
    showAlertCreate() {
      this.showSuccessAlert = true;
      this.alertMessage = "Customer was created successfully!";
    },
    showAlertUpdate() {
      this.showSuccessAlert = true;
      this.alertMessage = "Customer was updated successfully";
    },
    showDeleteModal(id) {
      this.$refs["delete-customer-modal"].show();
      this.customerId = id;
    },
    closeDeleteModal() {
      this.$refs["delete-customer-modal"].hide();
    },
    showDeleteSuccessModal() {
      this.showSuccessAlert = true;
      this.alertMessage = "Customer was deleted successfully!";
    },
  },
};
</script>

<style>
.action-item:hover {
  cursor: pointer;
}
</style>