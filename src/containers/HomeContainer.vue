<template>
  <div class="home-layout">
    <h1 class="h2">Home : Tokamak Network</h1>
  </div>
</template>

<script>
import * as d3 from 'd3';
import { getNodes } from '@/api/index.js';

export default {
  data () {
    return {
      node: [],
      link: [],
    };
  },
  create () {
    this.setData ();
  },
  methods: {
    async setData () {
      const datass = await getNodes();

      const width = 960,
        height = 500;

      const svg = d3
        .select('#home-main-dom')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      const force = d3.layout
        .force()
        .gravity(0.05)
        .distance(130)
        .charge(-110)
        .size([width, height]);

      force
        .nodes(datass.nodes)
        .links(datass.links)
        .start();

      const link = svg
        .selectAll('.link')
        .data(datass.links)
        .enter()
        .append('line')
        .attr('class', 'link')
        .style('stroke-width', function (d) {
          return Math.sqrt(d.weight);
        });

      const node = svg
        .selectAll('.node')
        .data(datass.nodes)
        .enter()
        .append('g')
        .attr('class', 'node')
        .call(force.drag);

      node.append('circle').attr('r', '5');

      node
        .append('text')
        .attr('dx', 12)
        .attr('dy', '.35em')
        .text(function (d) {
          return d.name;
        });

      force.on('tick', function () {
        link
          .attr('x1', function (d) {
            return d.source.x;
          })
          .attr('y1', function (d) {
            return d.source.y;
          })
          .attr('x2', function (d) {
            return d.target.x;
          })
          .attr('y2', function (d) {
            return d.target.y;
          });

        node.attr('transform', function (d) {
          return 'translate(' + d.x + ',' + d.y + ')';
        });
      });
    },
  },
};
</script>
