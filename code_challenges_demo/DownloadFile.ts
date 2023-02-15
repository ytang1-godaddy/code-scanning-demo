/*********************
 * Difficulty ★★★☆☆
 ********************/
// @ts-nocheck
import db from "./SQLConnector";
import decrypt from "./Decryptor";

interface User {
  username: string;
  password: string;
  email: string;
  isAdmin: boolean;
}
interface DownloadForm {
  userInfo?: User | undefined;
  fileName: string;
}

const DECRYPT_KEY = "aGVsbG8tc2Nob2ktd29ybGQhISEh";
export async function canDownload(formData: DownloadForm): Promise<boolean> {
  let email, pwd: string;
  try {
    const sqlQuery = "SELECT email, password FROM files WHERE name = ?";
    const res = await db.querySanitized(sqlQuery, [formData.fileName])[0];
    email = res.email;
    pwd = decrypt(DECRYPT_KEY)(res.password);
  } catch (err) {
    return false;
  }

  if (
    (formData.userInfo && formData.userInfo.email !== email) ||
    (formData.userInfo && formData.userInfo.password !== pwd)
  ) {
    return false;
  }

  return true;
}
