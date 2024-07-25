import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  try {
    const signUpPromise = signUpUser(firstName, lastName);
    const uploadPhotoPromise = uploadPhoto(fileName);

    const results = await Promise.allSettled([signUpPromise, uploadPhotoPromise]);

    return results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : result.reason,
    }));
  } catch (error) {
    return [{
      status: 'rejected',
      value: error,
    }];
  }
}
