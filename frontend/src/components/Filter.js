import React from 'react'

const Filter = ({ onSelect }) => {
    const handleSelect = (event) => {
        const value = event.target.value === 'null' ? null : event.target.value
        onSelect(value)
    }

    return (
        <div className=' p-1'>
            <label htmlFor='statusFilter' className='text-sm pr-2'>Filter</label>

            <select name='statusFilter' id='statusFilter' onChange={handleSelect} className='text-sm cursor-pointer border-black'>
                <option value='null'>All</option>
                <option value='free'>Free</option>
                <option value='paid'>Paid</option>
            </select>
        </div>
    );
}

export default Filter;