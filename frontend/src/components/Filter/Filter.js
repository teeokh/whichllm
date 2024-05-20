import React, { useState, useEffect } from 'react'

const Filter = ({ onSelect }) => {
    const handleSelect = (event) => {
        const value = event.target.value === 'null' ? null : event.target.value
        onSelect(value)
    }

    return ( 
        <div className='App'>
            <label htmlFor='statusFilter'>Filter</label>

            <select name='statusFilter' id='statusFilter' onChange={handleSelect}>
                <option value='null'>All</option>
                <option value='free'>Free</option>
                <option value='paid'>Paid</option>
            </select>
        </div>
    );
}
 
export default Filter;