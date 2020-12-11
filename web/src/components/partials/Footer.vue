<template>
  <div class="footer-bottom p-3">
    <b-container>
      <b-row>
        <b-col>
          <img :src="require('@/assets/logo_gba_footer_blanco.svg')" class="img-fluid w-50"/>
        </b-col>
        <b-col class="mt-4">
          <ul class="list-inline social-buttons">
            <li class="list-inline-item">
              <a href="#">
                <font-awesome-icon :icon="['fab', 'facebook']"/>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <font-awesome-icon :icon="['fab', 'twitter']"/>
              </a>
            </li>
            <li class="list-inline-item">
              <a href="#">
                <font-awesome-icon :icon="['fab', 'instagram']"/>
              </a>
            </li>
          </ul>
        </b-col>
        <b-col>
          <br/>
          <span class="text-white p-4 font-weight-bold text-copy">&copy; GRUPO 56</span>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>


<script>
export default {
  name: 'Footer',
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');

.footer-bottom {
  width: 100%;
  position: absolute;
  bottom: 0;
  background-color: #212529;
}

a {
  color: #6c757d;
}

a:hover {
  color: #fec503;
  text-decoration: none;
}

::selection {
  background: #fec503;
  text-shadow: none;
}

ul.social-buttons {
  margin-bottom: 0;
}

ul.social-buttons li a:active,
ul.social-buttons li a:focus,
ul.social-buttons li a:hover {
  background-color: darkcyan;
}

ul.social-buttons li a {
  font-size: 20px;
  line-height: 40px;
  display: block;
  width: 40px;
  height: 40px;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  transition: all 0.3s;
  color: #fff;
  border-radius: 100%;
  outline: 0;
  background-color: #1a1d20;
}

.text-copy {
  font-size: 90%;
  line-height: 40px;
  margin-bottom: 0;
  text-transform: none;
  font-family: Montserrat, "Helvetica Neue", Helvetica, Arial, sans-serif;
}


</style>