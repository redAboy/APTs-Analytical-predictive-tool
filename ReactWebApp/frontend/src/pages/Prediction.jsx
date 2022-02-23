import React, {useState} from 'react'

import * as PredictionResult from '../components/predictions'

const API = process.env.REACT_APP_API;

const Prediction = () => {

    let [country1, setCountry1] = useState("RUS")
    let [country2, setCountry2] = useState("GBR")
    let [year, setYear] = useState("2021")

    let[result, setResult] = useState("PredictionResultVoid")
    let[prediction, setPrediction] = useState({})

    const PredictionComponent = PredictionResult[result]
    
    const getPrediction = async (country1, country2, year) => {
        
        const prediction_response = await fetch(`${API}/prediction/${country1}/${country2}/${year}`, {
            method: 'GET',
        })
        const prediction_json = await prediction_response.json();
        console.log(prediction_json)
        
        setPrediction(prediction_json)
        setResult("PredictionResult")
    }

    return (
        <div>
            <div className="row">
                <div className="col-4">
                    <div className="card full-height">
                        <div className="card__body">
                            <label>Select Attacking Country</label>
                            <select name="" id="" onChange={(e) => {setCountry1(e.target.value); console.log(e.target.value)}}>
                                <option value="RUS">RUS</option>
                                <option value="BEL">BEL</option>
                                <option value="UKR">UKR</option>
                                <option value="BLR">BLR</option>
                                <option value="GBR">GBR</option>
                                <option value="IRN">IRN</option>
                                <option value="PRK">PRK</option>
                                <option value="IND">IND</option>
                                <option value="KHM">KHM</option>
                                <option value="CHN">CHN</option>
                                <option value="JPN">JPN</option>
                                <option value="KOR">KOR</option>
                                <option value="SAU">SAU</option>
                                <option value="AFG">AFG</option>
                                <option value="VNM">VNM</option>
                                <option value="PAK">PAK</option>
                                <option value="SAS">SAS</option>
                                <option value="ARE">ARE</option>
                                <option value="GEO">GEO</option>
                                <option value="MEA">MEA</option>
                                <option value="AZE">AZE</option>
                                <option value="SYR">SYR</option>
                                <option value="TUR">TUR</option>
                                <option value="KAZ">KAZ</option>
                                <option value="USA">USA</option>
                                <option value="COL">COL</option>
                                <option value="ARG">ARG</option>
                                <option value="BRA">BRA</option>
                                <option value="AUS">AUS</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div className="col-4">
                    <div className="card full-height">
                        <div className="card__body">
                            <label>Select Affected Country</label>
                            <select name="" id="" onChange={(e) => {setCountry2(e.target.value); console.log(e.target.value)}}>
                                <option value="GBR">GBR</option>
                                <option value="BEL">BEL</option>
                                <option value="POL">POL</option>
                                <option value="FIN">FIN</option>
                                <option value="FRA">FRA</option>
                                <option value="IRL">IRL</option>
                                <option value="NOR">NOR</option>
                                <option value="SWE">SWE</option>
                                <option value="ESP">ESP</option>
                                <option value="DEU">DEU</option>
                                <option value="GRC">GRC</option>
                                <option value="ITA">ITA</option>
                                <option value="CHE">CHE</option>
                                <option value="DNK">DNK</option>
                                <option value="EST">EST</option>
                                <option value="AUT">AUT</option>
                                <option value="UKR">UKR</option>
                                <option value="BGR">BGR</option>
                                <option value="ALB">ALB</option>
                                <option value="BLR">BLR</option>
                                <option value="CYP">CYP</option>
                                <option value="NLD">NLD</option>
                                <option value="RUS">RUS</option>
                                <option value="LVA">LVA</option>
                                <option value="HRV">HRV</option>
                                <option value="ISR">ISR</option>
                                <option value="JOR">JOR</option>
                                <option value="CHN">CHN</option>
                                <option value="JPN">JPN</option>
                                <option value="SAU">SAU</option>
                                <option value="SGP">SGP</option>
                                <option value="IDN">IDN</option>
                                <option value="IND">IND</option>
                                <option value="MYS">MYS</option>
                                <option value="OMN">OMN</option>
                                <option value="PHL">PHL</option>
                                <option value="THA">THA</option>
                                <option value="TUR">TUR</option>
                                <option value="BGD">BGD</option>
                                <option value="MDV">MDV</option>
                                <option value="PAK">PAK</option>
                                <option value="AFG">AFG</option>
                                <option value="ARE">ARE</option>
                                <option value="QAT">QAT</option>
                                <option value="BHR">BHR</option>
                                <option value="KWT">KWT</option>
                                <option value="LBN">LBN</option>
                                <option value="IRQ">IRQ</option>
                                <option value="MMR">MMR</option>
                                <option value="MNG">MNG</option>
                                <option value="GEO">GEO</option>
                                <option value="KHM">KHM</option>
                                <option value="NPL">NPL</option>
                                <option value="KAZ">KAZ</option>
                                <option value="ARM">ARM</option>
                                <option value="YEM">YEM</option>
                                <option value="AZE">AZE</option>
                                <option value="TJK">TJK</option>
                                <option value="TKM">TKM</option>
                                <option value="LKA">LKA</option>
                                <option value="UZB">UZB</option>
                                <option value="MLI">MLI</option>
                                <option value="ZAF">ZAF</option>
                                <option value="ZAF">ZAF</option>
                                <option value="EGY">EGY</option>
                                <option value="KEN">KEN</option>
                                <option value="RWA">RWA</option>
                                <option value="SDN">SDN</option>
                                <option value="NER">NER</option>
                                <option value="NGA">NGA</option>
                                <option value="SOM">SOM</option>
                                <option value="CAN">CAN</option>
                                <option value="USA">USA</option>
                                <option value="BRA">BRA</option>
                                <option value="CUB">CUB</option>
                                <option value="MEX">MEX</option>
                                <option value="ARG">ARG</option>
                                <option value="PER">PER</option>
                                <option value="COL">COL</option>
                                <option value="ECU">ECU</option>
                                <option value="CHL">CHL</option>
                                <option value="GTM">GTM</option>
                                <option value="AUS">AUS</option>
                                <option value="NZL">NZL</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div className="col-4">
                    <div className="card full-height">
                        <div className="card__body">
                            <label>Select Year</label>
                            <select name="" id="" onChange={(e) => {setYear(e.target.value); console.log(e.target.value)}}>
                                <option value="2021">2021</option>
                                <option value="2020">2020</option>
                                <option value="2019">2019</option>
                                <option value="2018">2018</option>
                                <option value="2017">2017</option>
                                <option value="2016">2016</option>
                                <option value="2015">2015</option>
                                <option value="2014">2014</option>
                                <option value="2013">2013</option>
                                <option value="2012">2012</option>
                                <option value="2011">2011</option>
                                <option value="2010">2010</option>
                                <option value="2009">2009</option>
                                <option value="2008">2008</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div className="col-1">
                    <div className="card card_button">
                        <div className="card__body">
                            <button className="card_button_text" onClick={() => {getPrediction(country1, country2, year)}}>Predict</button>
                        </div>
                    </div>
                </div>
            </div>
            <PredictionComponent
                prediction = {prediction}
            />
        </div>
    )
}

export default Prediction