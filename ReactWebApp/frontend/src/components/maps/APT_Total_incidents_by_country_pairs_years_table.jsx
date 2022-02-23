import React from 'react'
import KeplertGlReducer from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware} from "redux";
import {taskMiddleware} from "react-palm/tasks";
import {Provider} from "react-redux";

import Mapdispatcher from "./APT_Total_incidents_by_country_pairs_years_table_dispatcher";

const reducers = combineReducers({
  keplerGl: KeplertGlReducer
});

const APT_Total_incidents_by_country_pairs_years_table_store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

const Map = (props) => {

    return (
        <Provider store={APT_Total_incidents_by_country_pairs_years_table_store}>
          <Mapdispatcher
              collection = {props.collection}
          />
        </Provider>
    )
}

export default Map


