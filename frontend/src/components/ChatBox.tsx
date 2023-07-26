import React, { useState } from 'react';
import { PromptAi } from 'src/hooks/PromptAi';
import { Message } from 'src/types/Message';
import MessageBox from './MessageBox';
import LoadingMessage from './LoadingMessage';

const ChatBox = () => {
    const [message, setMessage] = useState<string>('');
    const [messages, setMessages] = useState<Message[]>([]);
    const [loading, setLoading] = useState<boolean>(false);

    const sendMessage = async (message: string) => {
        setMessages((messages) => {
            return [
                ...messages,
                {
                    content: message,
                    isSentByUser: true,
                },
            ];
        });
        setLoading(true);
        console.log(messages);
        PromptAi(message, `${import.meta.env.VITE_PROMPT_API}`);
        // const response = await ChatbotService.sendMessage(message);
        // Open the URL in the current tab
        setMessages((messages) => {
            return [
                ...messages,
                {
                    content: 'chatbox reponse here',
                    isSentByUser: false,
                },
            ];
        });
        setLoading(false);
    };

    return (
        <div id='ui-container' className='w-screen h-auto min-h-screen flex justify-center items-center'>
            <div className='p-4 bg-white shadow-lg rounded-lg sm:h-screen sm:w-screen lg:h-auto lg:w-4/6 xl:w-[682px] grid grid-cols-1 grid-rows-[1fr,min-content]'>
                <div className='flex flex-col mb-4 space-y-6'>
                    <div className='chat bg-green'>
                        <div className='flex items-center space-x-4'>
                            <img
                                src='https://source.unsplash.com/600x600/?abstract'
                                alt='User Avatar'
                                className='w-10 h-10 rounded-full'
                            />
                            <h2 className='text-lg font-semibold'>Chatbot Name</h2>
                        </div>
                        <div>
                            <div className='flex flex-col space-y-2'>
                                {messages.map((message, index) => {
                                    return <MessageBox key={index} message={message} />;
                                })}
                                {loading && <LoadingMessage />}
                            </div>
                        </div>
                    </div>
                </div>
                <div className='flex items-center mt-4'>
                    <input
                        className='flex-grow px-2 py-1 border border-gray-300 rounded'
                        type='text'
                        value={message}
                        disabled={loading}
                        placeholder='What shutter speed and aperture should I use for portraits?'
                        onChange={(event) => {
                            setMessage(event.currentTarget.value);
                        }}
                        onKeyDown={async (event) => {
                            if (event.key === 'Enter') {
                                event.preventDefault();
                                const message = event.currentTarget.value;
                                sendMessage(message);
                                setMessage('');
                            }
                        }}
                    />
                    <button
                        className='px-4 py-2 ml-2 text-sm font-semibold text-white bg-blue-500 hover:bg-blue-600 rounded'
                        disabled={loading}
                        onClick={(event) => {
                            event.preventDefault();
                            sendMessage(message);
                            setMessage('');
                        }}
                    >
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ChatBox;
