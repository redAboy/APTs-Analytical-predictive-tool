import React, {useState} from 'react'

import * as Analytic_Components from '../components/analytics'

const API = process.env.REACT_APP_API;

const Analytics = () => {

    const [collection, setCollection] = useState()

    const [component, setComponent] = useState('AnalyticsVoid')

    const [headers, setHeaders] = useState()

    const getcollectionHeader = async (collection) => {
        if (!collection)
            return
        const doc_list = await fetch(`${API}/analytics/${collection}`, {
            method: 'GET',
        })
        const doc_list_data = await doc_list.json();
        setHeaders(doc_list_data.headers)
        setComponent("Analytics");
    }


    const Analytic = Analytic_Components[component]

    return (
        <div>
            <h2 className='page-header'>{collection}</h2>
            <div className="row">
                <div className="col-6">
                    <div className="card">
                        <div className="card__body">
                            <label>Select Collection</label>
                            <select name="" id="" onChange={(e) => {setCollection(e.target.value); console.log(e.target.value); getcollectionHeader(e.target.value);}}>
                                <option value="APT_Total_incident_by_group">APT_Total_incident_by_group</option>
                                <option value="APT_Total_incident_received_by_country_table">APT_Total_incident_received_by_country_table</option>
                                <option value="APT_Total_incident_sent_by_country_table">APT_Total_incident_sent_by_country_table</option>
                                <option value="APT_Total_incidents_sent_by_years_table">APT_Total_incidents_sent_by_years_table</option>
                                <option value="APT_Total_incidents_by_country_pairs_years_table">APT_Total_incidents_by_country_pairs_years_table</option>
                                <option value="APT_Total_incidents_by_country_pairs_table">APT_Total_incidents_by_country_pairs_table</option>
                                <option value="APT_GEO_Context_2021_missing">APT_GEO_Context_2021_missing</option>
                                <option value="APT_GEO_Context_complete">APT_GEO_Context_complete</option>
                                <option value="APT_Group_Incidents">APT_Group_Incidents</option>
                                <option value="APT_Group_Incidents_CAMEO">APT_Group_Incidents_CAMEO</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            {headers && component && <Analytic
                collection = {collection}
                headers = {headers}
            />}
        </div>
    )
}

export default Analytics