import React from 'react';
import { Message } from 'src/types/Message';

const MessageBox = ({ message }: { message: Message }) => {
    const response = !message.isSentByUser ? message.content : null;
    const formattedResponse = response?.split('\n');

    return (
        <>
            {message.isSentByUser && (
                <div className='flex items-end space-x-3 space-y-3'>
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
                <div className='w-full flex items-end justify-end space-x-3 space-y-3'>
                    <div className='p-2 bg-blue-100 rounded-lg'>
                        {/* <p className='text-blue-600'>{message.content}</p> */}
                        {formattedResponse?.map((line: string, i) => {
                            return line === '' ? (
                                <br />
                            ) : (
                                <p key={i} className='text-blue-600'>
                                    {line}
                                </p>
                            );
                        })}
                    </div>
                    <img
                        src='https://source.unsplash.com/600x600/?kodak'
                        alt='Bot Avatar'
                        className='w-10 h-10 rounded-full'
                    />
                </div>
            )}
        </>
    );
};

export default MessageBox;
