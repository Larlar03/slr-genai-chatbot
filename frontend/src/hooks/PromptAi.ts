import axios from 'axios';
import { PromptAiQuestion } from 'src/types/PromptAiQuestion';
import { PromptAiResponse } from 'src/types/PromptAiResponse';

export const PromptAi = async (messageString: string, chatId: string, apiUrl: string): Promise<PromptAiResponse> => {
    console.log(`Sending message: ${messageString}, chatId: ${chatId}`);

    const requestBody: PromptAiQuestion = {
        chatId: chatId,
        message: messageString,
    };

    const response = await axios.post(apiUrl, requestBody).catch((error) => {
        console.error(error);
    });

    return response?.data.answer;
};
