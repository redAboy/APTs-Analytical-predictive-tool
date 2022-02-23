import React, {useState} from 'react'

import * as Maps_components from '../components/maps';

const Maps = () => {

    let [collection, setCollection] = useState("APT_Total_incident_sent_by_group")

    const Map = Maps_components[collection]

    return (
        <div>
            <div className="row">
                <div className="col-6">
                    <div className="card">
                        <div className="card__body">
                            <label>Select Collection</label>
                            <select name="" id="" onChange={(e) => {setCollection(e.target.value); console.log(e.target.value)}}>
                                <option value="APT_Total_incident_sent_by_group">APT_Total_incident_sent_by_group</option>
                                <option value="APT_Total_incident_received_by_country">APT_Total_incident_received_by_country</option>
                                <option value="APT_Total_incident_sent_by_country">APT_Total_incident_sent_by_country</option>
                                <option value="APT_Total_incident_sent_by_years">APT_Total_incident_sent_by_years</option>
                                <option value="APT_Total_incidents_by_country_pairs_table">APT_Total_incidents_by_country_pairs_table</option>
                                <option value="APT_Total_incidents_by_country_pairs_years_table">APT_Total_incidents_by_country_pairs_years_table</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            {<Map
                collection = {collection}
            />}
        </div>
    )
}

export default Maps