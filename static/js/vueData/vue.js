import { CoreVue } from "../vueData/coreObjects/exportVue.js";
import { loader } from "../vueData/coreComponents/loader.js";

const { createApp } = Vue;

/*Objeto constructor estrategia: CORE*/
/*en otro archivo*/

/*Utilizar el método createApp y asignarlo*/
const app = createApp(CoreVue);

/*Montar la app*/
app.mount ("#app");