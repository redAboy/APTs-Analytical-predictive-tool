import React from 'react'
import Chart from 'react-apexcharts'

const PredictionResult = (props) => {

    return (
        <React.Fragment>
            <h1>Prediction Results</h1>
            <div className="row">
                <div className="col-2 result">
                    <h3>Prediction</h3>
                    <div className="card result_values">
                        <div className="card__body">
                            <p className="result_text">{props.prediction.prediction.toFixed(4)} ~ {props.prediction.deviation.toFixed(4)}</p>
                            <br/>
                            <p>incidents</p>
                        </div>
                    </div>
                </div>
                <div className="col-2 result">
                    <h3>Real Incidents</h3>
                    <div className="card result_values">
                        <div className="card__body">
                            <p className="result_text">{props.prediction.real_incidents}</p>
                            <br/>
                            <p>incidents</p>
                        </div>
                    </div>
                </div>
                <div className="col-2 result">
                    <h3>Prediction Error</h3>
                    <div className="card result_values">
                        <div className="card__body">
                            <p className="result_text">{props.prediction.prediction_error}</p>
                            <br/>
                            <p>incidents</p>
                        </div>
                    </div>
                </div>
                <div className="col-6 result">
                    <Chart
                        options={props.prediction.chartOptions.options}
                        series={props.prediction.chartOptions.series}
                        type='line'
                        height='100%'

                    />
                </div>
            </div>
        </React.Fragment>
    )
}

export default PredictionResult
