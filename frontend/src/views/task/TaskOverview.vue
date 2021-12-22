<template>
  <div>
    <b-row class="text-center">
      <b-col>
        <div
          class="filter-card p-3"
          :class="{
            'bg-active-filter': totalIsActive,
            'bg-light': !totalIsActive,
          }"
          @click="totalTasksIsActiveFilter"
        >
          <h6>Total Tasks</h6>
          <h4>
            <strong>{{ totalTasks }}</strong>
          </h4>
        </div>
      </b-col>
      <b-col>
        <div
          class="filter-card p-3"
          :class="{
            'bg-active-filter': activeIsActive,
            'bg-light': !activeIsActive,
          }"
          @click="activeTasksIsActiveFilter"
        >
          <h6>Active Tasks</h6>
          <h4>
            <strong>{{ activeTasks }}</strong>
          </h4>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "TaskOverview",
  props: {
    totalTasks: Number,
    activeTasks: Number,
  },
  data() {
    return {
      totalIsActive: true,
      activeIsActive: false,
    };
  },
  methods: {
    totalTasksIsActiveFilter() {
      this.totalIsActive = true;
      this.activeIsActive = false;
      this.$emit("totalTasksIsActive");
    },
    activeTasksIsActiveFilter() {
      this.totalIsActive = false;
      this.activeIsActive = true;
      this.$emit("activeTaskIsActive");
    },
  },
};
</script>

<style>
.filter-card:hover {
  cursor: pointer;
  text-decoration: underline;
}

.bg-active-filter {
  background-color: #e9f1fe;
  color: #074297;
}
</style>