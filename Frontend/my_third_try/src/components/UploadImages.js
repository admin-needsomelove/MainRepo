/* import AWS from 'aws-sdk';
import base64 from 'react-native-base64'
import * as RNFS from 'react-native-fs';
import * as mime from 'react-native-mime-types';
import {env} from '../constants/environment';
import { Button } from 'react-native-paper';
import * as DocumentPicker from 'expo-document-picker';

 const uploadImageOnS3 = async (file) => {
    return new Promise(async (resolve, reject) => {
        const s3bucket = new AWS.S3({
            accessKeyId: env.accessKeyId,
            secretAccessKey: env.secretAccessKey,
            Bucket: env.awsBucket,
            signatureVersion: 'v4',
        });

        const base64_name = await fs.readFile(file.path, 'base64');
        const contentType = mime.lookup(file.path);
        const fileName = file.name || String(Date.now());
        const contentDeposition = 'inline;filename="' + filename + '"';
        const arrayBuffer = base64.decode(base64_name);

        s3bucket.createBucket(() => {
            const params = {
                Bucket: env.awsBucket,
                Key: fileName,
                Body: arrayBuffer,
                ContentDisposition: contentDeposition,
                ContentType: contentType,
            };
            s3bucket.upload(params, (err,data) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(data.Location);
                }
            })
        })
    })
} 

export default function FileSelector ({ route , navigation } ) {

    _pickDocument = async () => {
        let result = await DocumentPicker.getDocumentAsync({});
        alert(result.uri);
        console.log(result);
        }

    return (
        <Button
            title='Select Document'
            onPress={this._pickDocument}
        />
    )
} */