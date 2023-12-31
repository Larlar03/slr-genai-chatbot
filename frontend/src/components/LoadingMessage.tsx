import React from 'react';

const LoadingMessage = () => {
    return (
        <div className='items-end flex justify-end space-x-3 space-y-3 pl-2 mx-2 my-4 rounded-lg'>
            <div className='bg-gradient-to-r from-[#e0c3fc] to-[#8ec5fc] h-8 flex flex-row items-center justify-center text-base px-2 py-1 rounded-br-none rounded-lg'>
                <div className='animate-bounce w-3 h-3 bg-white rounded-full mr-2' />
                <div className='animate-[bounce_1s_infinite_200ms] w-3 h-3 bg-white rounded-full mr-2' />
                <div className='animate-[bounce_1s_infinite_400ms] w-3 h-3 bg-white rounded-full' />
            </div>
        </div>
    );
};

export default LoadingMessage;
