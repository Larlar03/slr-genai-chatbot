import React from 'react';
import { Message } from 'src/types/Message';

const MessageBox = ({ message }: { message: Message }) => {
    const response = !message.isSentByUser ? message.content : null;
    const formattedResponse = response?.split('\n');

    return (
        <>
            {message.isSentByUser && (
                <div className='flex items-end justify-end w-[99%]'>
                    <div className='p-2 bg-[#F8F6F8] rounded-lg '>
                        <p className='text-gray-900'>{message.content}</p>
                    </div>
                </div>
            )}
            {!message.isSentByUser && (
                <div className='flex flex-row items-end space-x-3 w-[99%]'>
                    <div>
                        <div className='w-10 h-10 bg-gradient-to-r from-[#e0c3fc] to-[#8ec5fc] rounded-full' />
                    </div>
                    <div className='p-2 bg-[#F1F0FF] rounded-lg rounded-bl-none'>
                        {formattedResponse?.map((line: string, i) => {
                            return line === '' ? (
                                <br />
                            ) : (
                                <p key={i} className='text-[#252136]'>
                                    {line}
                                </p>
                            );
                        })}
                    </div>
                </div>
            )}
        </>
    );
};

export default MessageBox;
