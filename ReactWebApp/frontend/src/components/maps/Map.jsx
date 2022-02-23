import React from 'react'
import KeplerGl from 'kepler.gl';
import {addDataToMap} from "kepler.gl/actions";
import {useDispatch} from "react-redux";
import useSwr from "swr";


const API = process.env.REACT_APP_API;

const Map = (props) => {
    console.log(props.collection)

    const dispatch = useDispatch();
    const { data } = useSwr("incidents", async () => {
      const response = await fetch(`${API}/maps/${props.collection}`, {
        method: 'GET',
    });
      const data = await response.json();
      return data;
    });

    React.useEffect(() => {
        if (data) {
          dispatch(
            addDataToMap({
              datasets: {
                info: {
                  label: "APT-Incidents",
                  id: "incidents"
                },
                data
              },
              option: {
                centerMap: true,
                readOnly: false
              },
              config: {}
            })
          );
        }
      }, [dispatch, data]);

    return (
        <React.Fragment>
            <KeplerGl
                id="incidents"
                mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_API}
                width={1550}
                height={window.innerHeight}
            />
        </React.Fragment>
    )
}

export default Map


