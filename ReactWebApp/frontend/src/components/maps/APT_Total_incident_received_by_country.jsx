import React from 'react'
import KeplertGlReducer from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware} from "redux";
import {taskMiddleware} from "react-palm/tasks";
import {Provider} from "react-redux";

import Mapdispatcher from "./APT_Total_incident_received_by_country_dispatcher";

const reducers = combineReducers({
  keplerGl: KeplertGlReducer
});

const APT_Total_incident_received_by_country_store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

const Map = (props) => {

    return (
        <Provider store={APT_Total_incident_received_by_country_store}>
          <Mapdispatcher
              collection = {props.collection}
          />
        </Provider>
    )
}

export default Map

