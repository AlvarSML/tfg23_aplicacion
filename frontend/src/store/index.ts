import { createStore, useStore as baseUseStore, Store } from 'vuex'
import { State } from './state'
import { InjectionKey } from 'vue'

import { mainModule } from "./main";
import { adminModule } from "./admin";
import { radiografias } from "./radiografias"


// define injection key
export const key: InjectionKey<Store<State>> = Symbol()

// Store en modulos
export const store = createStore<State>({
  modules: {
    main: mainModule,
    admin: adminModule,
    radiografias: radiografias
  }
})

// define your own `useStore` composition function
export function useStore () {
  return baseUseStore(key)
}