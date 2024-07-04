import * as React from 'react';
import { PieChart } from '@mui/x-charts/PieChart';
import { useEffect, useState } from 'react'
import axios from 'axios';

const Piechart = () => {
    const [pieChartData, setPieChartData] = useState([])

    useEffect(() => {
        const getData = async () => {
            const backend_url = process.env.REACT_APP_BACKEND_URL
            const response = await axios.get(`${backend_url}dashboard/piechart/`)
            const data = response.data.map((item, idx) => {
                return {
                    id: idx,
                    value: item.count,
                    label: item.user_agent
                }
            })

            setPieChartData(data)
        }

        getData()

    }, [])

    return (
        <PieChart
            series={[
                {
                    data: pieChartData,
                    highlightScope: { faded: 'global', highlighted: 'item' },
                    faded: { innerRadius: 30, additionalRadius: -30, color: 'gray' },
                },
            ]}
            width={500}
            height={250}
        />
    );
}

export default Piechart


