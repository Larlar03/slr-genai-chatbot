import React from 'react';
import { Message } from 'src/types/Message';

const MessageBox = ({ message }: { message: Message }) => {
    return (
        <>
            {message.isSentByUser && (
                <div className='flex items-start space-x-3 space-y-3'>
                    <img
                        src='https://source.unsplash.com/600x600/?colourful'
                        alt='User Avatar'
                        className='w-10 h-10 rounded-full'
                    />
                    <div className='p-2 bg-gray-100 rounded-lg'>
                        <p className='text-gray-600'>{message.content}</p>
                    </div>
                </div>
            )}
            {!message.isSentByUser && (
                <div className='flex items-start space-x-3 space-y-3'>
                    <img
                        src='https://source.unsplash.com/600x600/?abstract'
                        alt='Bot Avatar'
                        className='w-10 h-10 rounded-full'
                    />
                    <div className='p-2 bg-blue-100 rounded-lg'>
                        <p className='text-blue-600'>{message.content}</p>
                    </div>
                </div>
            )}
        </>
    );
};

export default MessageBox;
