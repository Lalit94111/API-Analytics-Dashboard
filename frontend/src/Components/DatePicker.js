import * as React from 'react';
import { DemoContainer } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

const BasicDatePicker = ({ label, onChange }) => {
    // const handleChange = (date) => {
    //     if (date) {
    //         console.log(date.format('YYYY-MM-DD'));
    //     } else {
    //         console.log('No date selected');
    //     }
    // };
    return (
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DemoContainer components={['DatePicker']}>
                <DatePicker label={label} onChange={onChange} />
            </DemoContainer>
        </LocalizationProvider>
    );
}

export default BasicDatePicker
