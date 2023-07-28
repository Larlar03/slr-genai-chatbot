import axios from 'axios';
import { PromptAiQuestion } from 'src/types/PromptAiQuestion';

export const PromptAi = async (messageString: string, chatId: string, apiUrl: string): Promise<string> => {
    console.log(`Sending message: ${messageString}, chatId: ${chatId}`);

    const requestBody: PromptAiQuestion = {
        chatId: chatId,
        message: messageString,
    };

    const response = await axios.post(apiUrl, requestBody).catch((error) => {
        console.error('Error making request:', error);
    });

    return response?.data.answer;
};
