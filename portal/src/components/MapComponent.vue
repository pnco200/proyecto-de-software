<template>
  <div>
    <ol-map
      :loadTilesWhileAnimating="true"
      :loadTilesWhileInteracting="true"
      style="height: 400px"
      @click="onClick"
    >
      <ol-view
        ref="view"
        :center="center"
        :rotation="rotation"
        :zoom="zoom"
        :projection="projection"
      />

      <ol-tile-layer>
        <ol-source-osm />
      </ol-tile-layer>

      <ol-vector-layer>
        <ol-source-vector>
          <ol-feature>
            <ol-geom-point :coordinates="coordinate"></ol-geom-point>
            <ol-style>
              <ol-style-circle :radius="radius">
                <ol-style-fill :color="fillColor"></ol-style-fill>
                <ol-style-stroke
                  :color="strokeColor"
                  :width="strokeWidth"
                ></ol-style-stroke>
              </ol-style-circle>
            </ol-style>
          </ol-feature>
        </ol-source-vector>
      </ol-vector-layer>
    </ol-map>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const props = defineProps(["coordinates", "contact_information"]);

const coordinate = ref(props.coordinates);
const center = ref([0, 0]); // Default center
const projection = ref("EPSG:4326");
const zoom = ref(10);
const rotation = ref(0);
const radius = ref(21);
const strokeWidth = ref(8);
const strokeColor = ref("red");
const fillColor = ref("white");

onMounted(() => {
  center.value = [coordinate.value[0] - 0.0001, coordinate.value[1]];
});

const onClick = () => {
  alert("Información de contacto: " + props.contact_information);
};
</script>