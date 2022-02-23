import React from 'react'
import KeplerGl from 'kepler.gl';
import {addDataToMap} from "kepler.gl/actions";
import {useDispatch} from "react-redux";
import useSwr from "swr";


const API = process.env.REACT_APP_API;

const Mapdispatcher = (props) => {
    console.log(props.collection)

    const dispatch = useDispatch();
    const { data } = useSwr("by_country_pairs_incidents", async () => {
      const response = await fetch(`${API}/maps/${props.collection}`, {
        method: 'GET',
    });
      const data = await response.json();
      console.log(data)
      return data;
    });

    React.useEffect(() => {
        if (data) {
          dispatch(
            addDataToMap({
              datasets: {
                info: {
                  label: "APT_Total_incidents_by_country_pairs_table",
                  id: "by_country_pairs_incidents"
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
        <div>
            <KeplerGl
                id="by_country_pairs_incidents"
                mapboxApiAccessToken={process.env.REACT_APP_MAPBOX_API}
                width={1550}
                height={window.innerHeight}
            />
        </div>
    )
}

export default Mapdispatcher


