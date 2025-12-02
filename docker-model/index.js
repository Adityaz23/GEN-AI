import OpenAI from "openai";
import 'dotenv/config';
const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
     baseURL: process.env.OPENAI_BASE_URL,
});

const response  = await client.chat.completions.create({
    model:process.env.OPENAI_MODEL,
   
    // ChatML format.
    messages:[
          { role: 'system', content: 'You are a helpful AI that solves math and answers questions.' },
        { 
            role: 'user', 
            content: `Hey, I am Aditya. 

        }
    ]
})
console.log(response.choices[0].message.content);